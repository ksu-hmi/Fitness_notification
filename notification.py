#will need to import these libraries to send notification but should already be installed since it's part of python library
import smtplib
from email.message import EmailMessage

#creating an email alert def function 
def email_alert(subject, body, to): 
    #creating the message from the library above
    msg = EmailMessage()
    #method on the message and set it so the body of the message passes through this function
    msg.set_content(body)
    #set the subject of the email 
    msg['subject'] = subject
    #set the to of the emation
    msg['to'] = to 
   

    #created a new gmail for the presentation - where the notification
    user = "melekwon.py@gmail.com" 
    msg['from'] = user
    password = "zkovulyeuiteehno"
    print("login success")

    #Where you use the SMTP library from above and set it to gmail's smtp server with port 587
    server = smtplib.SMTP("smtp.gmail.com",587)
    #now can work with the server
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()


if __name__ == '__main__':
    email_alert("Today's Schedule", "Hello world", "6785258726@tmomail.net")
    print("text has been sent")

    


