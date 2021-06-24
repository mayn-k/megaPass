import clipboard
from end import encPassword


def menu():
    print("-"*30)
    print(("-"*13) + "Menu"+ ("-" *13))
    print("1. Create new password")
    print("2. Find all sites and apps connected to an email")
    print("3. Find a password for a site or app")
    print("Q. Exit")
    print("-"*30)
    return input(": ")

def create():
    print("Please proivide the name of the site you want to generate a password for")
    appName = input()
    print("")
    print("Please provide a simple password for this site: ")
    passw = input()
    print("")
    encPassw,key = encPassword(passw)
    clipboard.copy(passw)
    print("-"*30)
    print("")
    print("Your password has now been created and copied to your clipboard")
    print("")
    print("-" *30)
    userEmail = input("Please provide a user email for this app or site: ")
    userName = input("Please provide a username for this app or site (if applicable): ")
    if userName == None:
        userName = ""
    url = input("Please paste the url to the site that you are creating the password for: ")
    #function to insert data (appName,encPass,key,userEmail,url) in accounts table

def findAccount():
    print("Please provide the email that you want to find account for:  ")
    userEmail = input()
    #sql select userEmail,appName,userName,url from accounts where userEmail = "xyz";
def find():
    print("Please proivide the name of the site or app you want to find the password to")
    appName = input()
    
    