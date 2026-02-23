# Email-Sending-in-Python




import smtplib
from email.message import EmailMessage

# -------- YOUR DETAILS --------
your_email = "your_gmail"
app_password = "hspp urhw josg ckpk"
Person_your_sending_email to's_email = "Person's_gmail"
# ------------------------------

# Create the email
msg = EmailMessage()
msg["Subject"] = "Hi!"
msg["From"] = your_email
msg["To"] = Person_your_sending_email to's_email
msg.set_content("Have a great day!")

# Connect to Gmail SMTP server and send
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(your_email, app_password)
    server.send_message(msg)

print("Email sent successfully!")
