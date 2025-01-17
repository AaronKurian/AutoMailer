from flask import Flask, render_template, request, redirect, url_for
import smtplib
import os
# import schedule
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import threading

app = Flask(__name__)

# Directory to store uploaded files temporarily
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to send the email
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

# # Function to schedule email
# def schedule_email(time_str, sender_email, sender_password, recipients, subject, body, attachments=[]):
#     schedule.every().day.at(time_str).do(send_email, sender_email, sender_password, recipients, subject, body, attachments)
#     print(f"Email scheduled at {time_str}")
#     while True:
#         schedule.run_pending()
#         time.sleep(1)

# Route to the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/send', methods=['POST'])
def send():
    sender_email = request.form['sender_email']
    sender_password = request.form['sender_password']
    recipients = request.form['recipients'].split(',')
    subject = request.form['subject']
    body = request.form['body']
    attachments = []

    # Save uploaded files
    if 'attachments' in request.files:
        files = request.files.getlist('attachments')
        for file in files:
            if file.filename != '':
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                file.save(filepath)
                attachments.append(filepath)

    choice = request.form['schedule']
    if choice == 'yes':
        time_str = request.form['time']
        # Run the scheduling function in a separate thread to avoid blocking the main thread
        threading.Thread(target=schedule_email, args=(time_str, sender_email, sender_password, recipients, subject, body, attachments)).start()
        return f"Email scheduled for {time_str}!"
    else:
        send_email(sender_email, sender_password, recipients, subject, body, attachments)
        return "Email sent successfully!"

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(host='0.0.0.0', port=8080, debug=True)
