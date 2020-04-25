import random
Email=input("enter the your email::-")
passwrd=input("Enter 10 digits strong password:::-")
usernamelen=6
username=[]
password=[]
passlen=6
for i in range(3):
    u="".join(random.sample(Email,usernamelen))
    username.append(u)
for j in range(3):
    p="".join(random.sample(passwrd,passlen))
    password.append(p)
print("Select only one username",username)
print("Select only one password",password)
user=int(input("Enter number which you want to select one username:::-"))
pas=int(input("Enter the number which you want to select one password:::-"))
for i in range(len(username)):
    if user==i:
        print("Your Username:::-",username[i])
    else:
        pass
for j in range(len(passwrd)):
    if pas==j:
        print("Your Password:::-",password[j])
    else:
        pass

