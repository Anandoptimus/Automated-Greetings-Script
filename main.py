import smtplib
from datetime import date
from twilio.rest import Client
from secretkeys import from_mail, password, to_mail, client_no, your_no, Account_id, account_token

ACCOUNT_ID = Account_id
AUTH_TOKEN = account_token
# client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
client = Client(username=ACCOUNT_ID, password=AUTH_TOKEN)

# this is the Twilio sandbox testing number
from_whatsapp_number = f'whatsapp:{client_no}'
# replace this number with your own WhatsApp Messaging number
to_whatsapp_number = f'whatsapp:{your_no}'

email = from_mail
password = password
to_email = to_mail

message = "hey Anand! hope you doing well, so i have come to remind you that you are awesome " \
          "you are doing great, make your limit limitless, face challenges, " \
          "God always with you and within you, take this motivation and " \
          "complete what you are aiming for "
now = date.today()
now = str(now)
today_date = now.split("-")[2]

if today_date == "20":
    client.messages.create(body=message,
                           from_=from_whatsapp_number,
                           to=to_whatsapp_number)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs=to_email,
                            msg=message)






