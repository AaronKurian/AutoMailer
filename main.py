import smtplib
import schedule
import time
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(sender_email, sender_password, recipients, subject, body, attachments=[]):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = ", ".join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        for file in attachments:
            if os.path.exists(file):
                with open(file, "rb") as attachment:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(file)}")
                    msg.attach(part)
            else:
                print(f"File not found: {file}")
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipients, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

def schedule_email(time_str, sender_email, sender_password, recipients, subject, body, attachments=[]):
    schedule.every().day.at(time_str).do(send_email, sender_email, sender_password, recipients, subject, body, attachments)
    print(f"Email scheduled at {time_str}")
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    sender_email = input("Enter your email: ")
    sender_password = input("Enter your password: ")
    recipients = input("Enter recipient emails (comma separated): ").split(',')
    subject = input("Enter email subject: ")
    body = input("Enter email body: ")
    attachments = input("Enter file paths (comma separated, or leave blank if none): ").split(',') if input("Do you want to attach files? (yes/no): ").strip().lower() == "yes" else []
    
    choice = input("Do you want to schedule the email? (yes/no): ").strip().lower()
    if choice == "yes":
        time_str = input("Enter time in HH:MM format (24-hour format): ")
        schedule_email(time_str, sender_email, sender_password, recipients, subject, body, attachments)
    else:
        send_email(sender_email, sender_password, recipients, subject, body, attachments)
