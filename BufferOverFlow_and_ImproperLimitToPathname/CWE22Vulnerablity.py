"""
Name: Hiren Shah
Date: 3/27/21
Purpose:This is the vulnerable code for CWE 22 Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal)
Here the user enters in the username and the path will grab any username and read out their text file without checking for constraints.
"""
def loadUserProfile(username):
    print("")
    with open("/home/ec2-user/environment/.c9/SDEV325_Assignment3/Data/UserProfiles/"+username + '.txt') as file:
        print("====== " + username + " profile ======")
        for line in file:
            print(line)



print("---- Add Friend ----")
username = input("Username: ")

loadUserProfile(username)
