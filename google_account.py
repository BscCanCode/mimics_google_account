print("Mimicking Google Account")
print("What would you like to do?")
print("1.Create_Account\n2.Login\n3.Exit")
details={"Name":[],"Surname":[],"email":[],"password":[]}

while True:
    try:
        n=int(input("Enter your choice: "))
        if n==3:
            print("Exit is success")
            break
        if n==1:
            print("Creating Account")
            print("------------------------------------------------------")
            x=input("Enter your name:")
            details["Name"].append(x)
            y=input("Enter your surname:")
            details["Surname"].append(y)
            print("Suggested email address")
            z=x+y+"@gmail.com"
            print(z)
            a=input("Would like to continue with suggested email address? yes/no:")
            if a=="no":
                c=input("Enter your email address:")
                if c.endswith("@gmail.com"):
                    print("Valid email address")
                    details["email"].append(c)
                else:
                    print("Invalid email address")
            elif a=="yes":
                print("Ok will go with suggested email")
                details["email"].append(z)
            else:
                print("Please do enter valid input!")
            b=input("Enter your password:")
            if len(b)>=8:
                print("Password is accepted!")
                details["password"].append(b)
                print("Password is stored successfully in our server")
            else:
                print("Password length must be equal to or greater than 8 characters!")
        elif n==2:
            print("Enter your login details below")
            print("---------------------------------------")
            d=input("Enter your email:")
            if d in details["email"]:
                e=input("Enter your password:")
                if e in details["password"]:
                    print("You have logged in successfully")
                else:
                    print("Incorrect password,try again")
            else:
                print("Entered email is not valid")
        else:
            print("Enter your choice between 1-3")
    except ValueError:
        print("Only int values are accepted!")
            
