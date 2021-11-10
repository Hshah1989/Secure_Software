"""
Name: Hiren Shah
Class: SDEV400_6380
Assignment: AWS CLI and DynamoDB
Purpose: Generates an interface which provides the user to 
execute actions on database
"""

import logging
import time
from botocore.exceptions import ClientError
import HW2_Q3Database



def main():
    # initialize the database 
    initDB()
    
    cont = "Y"
    while cont != "N" and cont != "n":
        # prompt for subject/catalog
        subject = input("Enter the Subject: ")
        
        if subject == "":
            while subject == "":
                print("Non empty subject is required!")
                subject = input("Enter the Subject: ")
        
        catalogNbr = input("Enter the CatalogNbr: ")
        
        if catalogNbr == "":
            while catalogNbr == "":
                print("Non empty catalogNbr is required!")
                catalogNbr = input("Enter the Subject: ")
        
        
        # get the result from the database
        result = searchDB(subject, catalogNbr)
        
        # print the result
        print(result)
        # prompt the user to continue
        cont = input("Enter any key to search again or N/n to exit: ")
        
    
def initDB():
    print("Initializing Database...")
    
    HW2_Q3Database.initialize()
    
    timeOutCounter = 0
    # wait until db is initialized
    while HW2_Q3Database.status() != "ACTIVE":
        time.sleep(1)
        timeOutCounter += 1
        if timeOutCounter > 20:  # time out after 20 seconds
            print("Operation taking long time")
            
    
    arrayofCourses = [['001','CMIS', 141, "Introductory Programming", 3],
        ['002','CMIS', 242, "Intermediate Programming", 3],
        ['003','CMIS', 320, "Relations DB Concepts and Applications", 3],
        ['004','SDEV', 300, "Building Secure Web Applications", 3],
        ['005','SDEV', 350, "Database Security", 3],
        ['006','SDEV', 360, "Secure Software Engineering", 3],
        ['007','SDEV', 400, "Secure Programming in the Cloud", 3],
        ['008','SDEV', 425, "Mitigating Software Vulnerabilities", 3],
        ['009','SDEV', 460, "Software Security Testing", 3],
        ['010','SDEV', 495, "Current Trends & Projects in Comp-Sci", 3]]
            
    HW2_Q3Database.add_items(arrayofCourses)
    print("Database successfuly initialized!")
    
def searchDB(subject, catalogNbr):
    try:
        data = HW2_Q3Database.search(subject.upper(), catalogNbr)
        
        if len(data) < 1:
            return "Course not found!"
        else:
            for d in data:
                if d["CatalogNbr"] == int(catalogNbr) and d["Subject"] == str(subject):
                    return "The title of " + str(subject) + " is " + str(catalogNbr) + " " + d["Title"] + "."
    except ClientError as error:
        return "Error searching database!"
    
    return "Course not found!"
    
main()