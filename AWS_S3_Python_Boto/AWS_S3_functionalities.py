import logging
import boto3
import random
import re
import sys
import os
from botocore.exceptions import ClientError

# creating a resource service with the s3 database
s3 = boto3.resource('s3')

# downloading a file from a bucket to the current directory
def download_obj(file_name, bucket):
    try:
        s3.meta.client.download_file(bucket, file_name, './%s'%file_name)
        print('successfully downloaded %s to current directory'%file_name)
    except ClientError:
        print('could not download file')
        
# copying a file form a bucket to another bucket
def copy_obj(bto, bfrom, file_name):
    copy = {
        "Bucket": bfrom,
        "Key": file_name
    }
    s3.meta.client.copy(copy, bto, file_name)
    print('successfully copied %s from %s to %s' %(file_name, bfrom, bto))

# creating a client service, deleting all objects in a bucket, and then deleting a bucket
def remove_bucket(bucket_name):
    s3c = boto3.client('s3')
    bucket = s3.Bucket(bucket_name)
    bucket.objects.all().delete()
    response=s3c.delete_bucket(Bucket=bucket_name)
    print('successfully deleted %s'%bucket_name)

# deleting a file from a bucket
def remove_obj(file_name, bucket_name):
    try:
        s3.Object(bucket_name, file_name).delete()
        print('deleted %s from %s' %(file_name, bucket_name))
    except ClientError:
        print('could not delete %s from %s' %(file_name, bucket_name))

# uploading a file to a bucket from our local instance
def upload_obj(path, bucket_name, object_name=None):
    if object_name is None:
        object_name = os.path.basename(path)

    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(path, bucket_name, object_name)
        print('\nUploaded %s to %s' %(path, bucket_name))
    except ClientError as e:
        logging.error(e)
        return False
    return True

            
# creating a bucket            
def create_bucket(bucket_name, region="us-east-1"):
    s3.create_bucket(Bucket=bucket_name)
    
# generating a 6 digit random number string
def random_six():
    out = ''
    for i in range(6):
        temp = random.randint(0, 9)
        out = out + str(temp)
    return out

# checking DNS compliance for bucket name
def check_compliance(s):
    findings = re.findall(r'(\.{2})|([^\w\d\.-]+)|(^[^\w\d]{1})|([^\w\d]{1}$)|(\-\.)|(\.\-)', s,
                          flags=re.I)  # check the compliance based on regex
    if len(findings) > 0:
        return False
    return True

# creating a name for a bucket
def create():
    fname = ''
    lname = ''
    check = ''
    compliant = False
    while not compliant:
        while True:
            # get first and last name
            name = input("Please enter first and last name separated by a space: ")
            try:
                temp = name.split(" ")  # take the name and split it up by spaces
                fname = temp[0]
                lname = temp[1]
            except ValueError:
                continue

            if fname[0].isalpha():  # check if the first character is a letter
                break

        # get a random six-digit suffix
        suffix = random_six()
        check = '%s%s-%s' % (fname, lname, suffix)  # take the three variables and put them in string as %s
        if not is_bucket(check):
            # check for compliance
            compliant = check_compliance(check)
    # create a bucket using DNS compliant name
    print(check)
    create_bucket(bucket_name=check)

# exit the program and print the date and time
def leave():
    from datetime import datetime
    t = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print('goodbye, %s' % t)  # prints datetime
    sys.exit(0)

# checking if the bucket exists
def is_bucket(bucket):
    try:
        s3.meta.client.head_bucket(Bucket = bucket)
        return True        
    except ClientError:
        print('%s does not exist' %bucket)
        return False
                
# calls the function 
def switch(usr):
    file_name = ''
    path = ''
    failed_bucket_check = False
    failed_os_check = False
    if usr == 1:
        create()
    elif usr == 2:
        file_name = input("Please enter a file name: ")
        bucket = input("Please enter a bucket name: ")
        failed_bucket_check = False if is_bucket(bucket) else True
        if os.path.exists(file_name):
            if not failed_bucket_check:
                upload_obj(file_name, bucket)
                return
        else:
            failed_os_check = True
            
    elif usr == 3:
        file_name = input("Please enter a file name: ")
        bucket = input("Please enter a bucket name: ")
        failed_bucket_check = False if is_bucket(bucket) else True
        if not failed_bucket_check:
            remove_obj(file_name, bucket)
            
    elif usr == 4:
        bucket = input("Please enter a bucket name: ")
        failed_bucket_check = False if is_bucket(bucket) else True
        if not failed_bucket_check:
            remove_bucket(bucket)
            
    elif usr == 5:
        bucket_to = input('Please enter a bucket you want to copy file to: ')
        if is_bucket(bucket_to):
            bucket_from = input('Please enter a bucket you want to copy file from: ')
            if is_bucket(bucket_from):
                file_name = input('Please enter a file name to copy: ')
                copy_obj(bucket_to, bucket_from, file_name)
                
        else:
            print('not a valid bucket')
            
            
    elif usr == 6:
        bucket = input("Please enter a bucket name: ")
        file_name = input("Please enter a file name: ")
        failed_bucket_check = False if is_bucket(bucket) else True
        if not failed_bucket_check:
            download_obj(file_name, bucket)
                
                
                
    elif usr == 7:
        leave()
    
    else:
        print("not a valid option")
    
    if failed_bucket_check:
        print('%s not a valid bucket'%bucket)
    if failed_os_check:
        print('%s not a valid file path'%file_name)
    
    
# main method
def main():
    while True:
        usr = input("What would you like to do?:"
                    "\n1.create a bucket\n2.put object in bucket\n3.delete object in bucket\n"
                    "4.delete bucket\n5. copy object from one bucket to another\n6.download an obj from bucket\n"
                    "7. exit program\n")
        try:
            temp = int(usr)
        except:
            continue
        if temp:
            switch(temp)

# For the main process        
if __name__ == "__main__":
    main()

