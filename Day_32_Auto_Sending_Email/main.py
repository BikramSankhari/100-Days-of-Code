import pandas, datetime, ssl, smtplib

MY_EMAIL = "popww619@gmail.com"
MY_PASSWORD = "vfyuqrhmwxtlsdwb"


def send_mail(receiver_name, receiver_email):
    with open("Birthday_Letter.txt") as file:
        letter = file.read()
        final_letter = letter.replace("[NAME]", receiver_name)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as mail:
        mail.login(MY_EMAIL, MY_PASSWORD)
        mail.sendmail(MY_EMAIL, receiver_email, msg=f"Subject:HAPPY BIRTHDAY\n\n{final_letter}")


today = datetime.datetime.now()
birthday_details = pandas.read_csv("Birthday_Details.csv")

for (index, data) in birthday_details.iterrows():
    if data.month == today.month and data.day == today.day:
        print(f"Today is {data['name']}'s Birthday.")
        send_mail(data['name'], data.mail)

