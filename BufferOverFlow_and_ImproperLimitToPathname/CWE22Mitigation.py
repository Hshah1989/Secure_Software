"""
Name: Hiren Shah 
Date: 3/27/21
Purpose:This is the mitigated code where a functions validates the expectedPath with the actualPath
"""

#  login function
import os
def loadUserProfile(username):
    print("")

    # get expected path and actual path
    expectedPath =  "/home/ec2-user/environment/.c9/SDE325_Assignment3/Data/UserProfiles"
    actualPath = "/home/ec2-user/environment/.c9/SDE325_Assignment3/Data/UserProfiles/" + username + '.txt'
    actualPath = os.path.realpath(actualPath)

    # check if actual path is within the expected directory

    # if validatePath returned false
    # we know the path the user gave is not correct
    if validatePath(expectedPath, actualPath) == False:
        print("Nice try punk. Ya aint getting nofin!")
        return


    with open(actualPath) as file:
        print("====== " + username + " profile ======")
        for line in file:
            print(line)

# check if the path the user entered goes to the appropriate directory
# return true if the path the user gave us is valid (ie in the userProfiles folder)
# return false if the path is not valid
def validatePath(expectedPath, autoPath):
    #print("expected:" + expectedPath)
    #print("Actual:" + autoPath)
  
    expectedFolders = expectedPath.split('/')
    actualFolders = autoPath.split('/')
    actualFolders.pop() # remove the userfile from the path (ex. user01.txt)
    
    #print(expectedFolders)
    #print(actualFolders)
    # both paths should be the same length now
    if len(actualFolders) != len(expectedFolders):
        return False

    # make sure each folder matches
    for i in range(0,len(expectedFolders)):
        # return false if a single folder in path does'nt match
        if expectedFolders[i] != actualFolders[i]:
            return False

    # if we made it here, the path must be valid
    return True









print("---- Add Friend ----")
username = input("Username: ")

loadUserProfile(username)
