import smtplib
from email.message import EmailMessage

# -------- YOUR DETAILS --------
your_email = "yourgmail@gmail.com"
app_password = "your_app_password_here"
someone_email = "someone@gmail.com"
# ------------------------------

# Create the email
msg = EmailMessage()
msg["Subject"] = "Hey!"
msg["From"] = your_email
msg["To"] = someone_email
msg.set_content("Have a great day!")

# Connect to Gmail SMTP server and send
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(your_email, app_password)
    server.send_message(msg)

print("Email sent successfully!")
