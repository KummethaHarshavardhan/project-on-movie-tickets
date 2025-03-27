import mysql.connector
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
url="  http://demo1867978.mockable.io/movie_data"
response=requests.get(url)
print(response.status_code)
if response.status_code==200:
    get_data=response.json()
    print(get_data)
else:
    print("not avialable data") 

mydb=mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='harsha6281240878',
    database='project tickets'
)
#print(mydb)
mycursor=mydb.cursor()
def login():
    moviename=input("enter movie name: ")
    screen=input("enter screen name: ")
    sql="select*from tickets_data where moviename=%s and screen=%s " 
    val=(moviename,screen)
    mycursor.execute(sql,val)
    result=mycursor.fetchone()
    if result:
        print(f"hi sir! the {moviename} movie  is avilabe")
        def devara():
            per_person=300
            number_of_persons=int(input("enter the number of persons: "))
            gst_amount=per_person+15
            total_amount=gst_amount*number_of_persons
            print(f"your amount is {total_amount},please go to screen-1 ")
            var=input("do you want book this ticket: ")
            if var=="yes":
                full_name=input("enter your full name : ")
                x=input("enter you emil_id : ")
                sender_email = "harshavardhan6281240878@gmail.com"
                receiver_email = x
                password = "okpf axmv octs zvrh"
                subject = "Total Bill"
                body = f"Your total bill is: ${total_amount}"
                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = receiver_email
                msg['Subject'] = subject
                msg.attach(MIMEText(body, 'plain'))
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, msg.as_string())
                server.quit()
                print("Email sent successfully!")
            else:
                print("thank you sir!")
        def pushpa():
            per_person=350
            number_of_persons=int(input("enter the number of persons: "))
            gst_amount=per_person+15
            total_amount=gst_amount*number_of_persons
            print(f"your amount is {total_amount},please go to screen-2 ")
            var=input("do you want book this ticket: ")
            if var=="yes":
                full_name=input("enter your full name : ")
                x=input("enter you emil_id : ")
                sender_email = "harshavardhan6281240878@gmail.com"
                receiver_email = x
                password = "okpf axmv octs zvrh"
                subject = "Total Bill"
                body = f"Your total bill is: ${total_amount}"
                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = receiver_email
                msg['Subject'] = subject
                msg.attach(MIMEText(body, 'plain'))
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, msg.as_string())
                server.quit()
                print("Email sent successfully!")
            else:
                print("thank you sir!")  
        def salaar():
            per_person=250
            number_of_persons=int(input("enter the number of persons: "))
            gst_amount=per_person+15
            total_amount=gst_amount*number_of_persons
            print(f"your amount is {total_amount},please go to screen-3 ")
            var=input("do you want book this ticket: ")
            if var=="yes":
                full_name=input("enter your full name : ")
                x=input("enter you emil_id : ")
                sender_email = "harshavardhan6281240878@gmail.com"
                receiver_email = x
                password = "okpf axmv octs zvrh"
                subject = "Total Bill"
                body = f"Your total bill is: ${total_amount}"
                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = receiver_email
                msg['Subject'] = subject
                msg.attach(MIMEText(body, 'plain'))
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, msg.as_string())
                server.quit()
                print("Email sent successfully!")
            else:
                print("thank you sir!")                 
        def kalki():
            per_person=300
            number_of_persons=int(input("enter the number of persons: "))
            gst_amount=per_person+15
            total_amount=gst_amount*number_of_persons
            print(f"your amount is {total_amount},please go to screen-3 ")
            var=input("do you want book this ticket: ")
            if var=="yes":
                full_name=input("enter your full name : ")
                x=input("enter you emil_id : ")
                sender_email = "harshavardhan6281240878@gmail.com"
                receiver_email = x
                password = "okpf axmv octs zvrh"
                subject = "Total Bill"
                body = f"Your total bill is: ${total_amount}"
                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = receiver_email
                msg['Subject'] = subject
                msg.attach(MIMEText(body, 'plain'))
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, msg.as_string())
                server.quit()
                print("Email sent successfully!")
            else:
                print("thank you sir!")              
        def main():
            choose_number=int(input("enter moviename number: "))
            if choose_number==1:
                devara()
            elif choose_number==2:
                pushpa()
            elif choose_number==3:
                salaar()
            elif choose_number==4:
                kalki()
            else:
                print("thank you") 
        main()           
    else:
        print(f"{moviename} not available")
login() 
'''
output:-
200
{'moviename1': 'devara', 'moviename2': 'pushpa', 'moviename3': 'salaar', 'moviename4': 'kalki'}
enter movie name: pushpa
enter screen name: s2
hi sir! the pushpa movie  is avilabe
enter moviename number: 2
enter the number of persons: 3
your amount is 1095,please go to screen-2 
do you want book this ticket: yes
enter your full name : harsha
enter you emil_id : harshavardhankummeth@gmail.com
Email sent successfully!
PS D:\kummetha harshavardhan\python> '''       