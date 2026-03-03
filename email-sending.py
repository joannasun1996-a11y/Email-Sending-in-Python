import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "Test Email"
msg["From"] = "your_email@gmail.com"
msg["To"] = "receiver@email.com"
msg.set_content("Hello from Python!")

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login("your_email@gmail.com", "your_app_password")
    server.send_message(msg)

print("Email sent!")
