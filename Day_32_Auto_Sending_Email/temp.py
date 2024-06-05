from email.message import EmailMessage
import ssl
import smtplib

my_email = "popww619@gmail.com"
my_password = "wftzytgpbgvaledj"
receiver_email = ["bikram1209@gmail.com", "suparnaraha97@gmail.com", "gymmersudipta@gmail.com"]

subject = "This is the subject"
body = '''
This is a Pythonic Email
'''

# e = EmailMessage()
# # e['To'] = ",".join(receiver_email)
# # e['From'] = my_email
# e['Subject'] = subject
# e.set_content(body)
#
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(my_email, my_password)
    smtp.sendmail(my_email, receiver_email, msg=f"")
