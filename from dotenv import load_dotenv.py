from dotenv import load_dotenv
import os
import random
import smtplib
import ssl
load_dotenv()
def send_emails(sender,reciever,recipient):
    password=os.environ('password')
    body_msg=f'''From:{sender}Subject:Your Secret Santa Present Hii!Your Secret Santa is:{recipient}!Remember you are going to have a beautiful gift!'''
    context=ssl.create_default_context()
    with smtplib.SMTP_SSL('snehapat699@gmail.com',546,context=context) as server:
        server.login(sender,password)
        server.sendmail(sender,reciever,body_msg)
        names_list=['Sneha','Shubhra']
        names_and_emails=[['Sneha','snehapat699@gmail.com'],['Shubhra','pathaksneha659@gmail.com']]
        if len(names_list)<=1:
            print('not enough people to start secret santa!')
            quit()
            first_name=names_and_emails[0][0]
            while len(names_list)>=2:
                send_emails('snehapat699@gmail.com',names_and_emails[0][1],names_and_emails[1][0])
                names_and_emails.pop(0)
                random.shuffle(names_and_emails)
                send_emails('snehapat699@gmail.com',names_and_emails[0][1],first_name)
                
    

