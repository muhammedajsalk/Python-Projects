def main():
    print("Welcome to the email slicer")
    print("")

    email_input = input("Enter your email eddress: ")
    
    (username,domain) = email_input.split("@")
    (domain,extention) = domain.split(".")

    print("username: ",username)
    print("domain: ",domain)
    print("Extention: ",extention)
    print("")

while True:
    main()