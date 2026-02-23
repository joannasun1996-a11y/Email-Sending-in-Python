# smtplib is a library, Simple Mail Transfer Protocol. It allows you to send emails using Gmail or other mail services.
import smtplib
# Without from email.message import EmailMessage, you cannot do msg = EmailMessage() msg["Subject"] = "Hi!" msg["From"] = your_email msg["To"] = Person_your_sending_email to's_email msg.set_content("Have a great day!")
from email.message import EmailMessage

# -------- YOUR DETAILS --------
your_email = "your_gmail"
app_password = "hspp urhw josg ckpk"
Person_your_sending_email to's_email = "Person's_gmail"
# ------------------------------

# Create the email. msg is short for message.
msg = EmailMessage()
msg["Subject"] = "Hi!"
msg["From"] = your_email
msg["To"] = Person_your_sending_email to's_email
msg.set_content("Have a great day!")

# Connect to Gmail SMTP server and send. Server is a computer on the internet, that does services.
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(your_email, app_password)
    server.send_message(msg)

print("Email sent successfully!")
