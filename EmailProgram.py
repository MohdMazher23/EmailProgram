#Sending Email to single or multiple users using python
#importing smtplib and giving alias name as sp
import smtplib as sp
#creating an object for smtplib class as obj
obj=sp.SMTP('smtp.gmail.com', 587)
# providing encryption
obj.starttls()
#login code
count=0
while count<3:
    count+=1
    try:
        print("Log in with your details")
        email=input("ENTER YOUR EMAIL ID:\n")
        password=input("Enter Your Password\n")
        obj.login(email,password)
        print("login Scccesull")
        break;
        
    except:
        print("-----Login Failed----Try Again----")
        n=input("Do you want to try again\n")
        if n!="yes":
            break

#Sending Email:

print("Sending Email")
to_email=[]

while True:
    recipients_email=input(("Enter recipients mail adress:\n"))
    #storing @gmail.com in reversed
    vaild_email=recipients_email[-1:-10:-1]
    #again reversing the string store in valid_email as gmail.com
    validation=vaild_email[-1::-1]
    #checking whether user enter correct domain of gmail
    if validation=="gmail.com":
        to_email.append(recipients_email)
    else:
        print("Please enter a valid email adress")
    con=input("Do you want to add another recipients email yes or no:\n")
    if con!="yes":
        break;
print(to_email)
subject=input("Enter Subject: ")
body=input("Enter your email body\n")
message="Subject:{}\n\n{}".format(subject,body)


#sending email to all recipientsts
try:
    obj.sendmail(email,to_email,message)
    print("Sended Succesfully")
except:
    print("Failed To send Email")
obj.quit()


"""
OUTPUT
#renaming the emails for security purpose
Log in with your details
ENTER YOUR EMAIL ID:
fromemailaddress
Enter Your Password
******
login Scccesull
Enter recipients mail adress:
hello123@gmail.com
Do you want to add another recipients email yes or no:
yes
Enter recipients mail adress:
robin123.mm@gmail.com
Do you want to add another recipients email yes or no:
yes
Enter recipients mail adress:
joey1234@gmail.com
Do you want to add another recipients email yes or no:
yes
Enter recipients mail adress:
home@gmail
Please enter a valid email adress
Do you want to add another recipients email yes or no:
no
['hello123@gmail.com', 'robin123.mm@gmail.com', 'joey1234@gmail.com']
Enter Subject: Application for leave
Enter your email body
Hi sir/madam i got fever so i cant attend the tommorow session
Sended Succesfully

"""