# Auto Mailer

Automailer is a Flask-based web application that allows users to send emails with or without attachments. The application supports file uploads and integrates with SMTP servers for email sending.
You can access the **live version** at:  
   **🔗 [https://automailer-k0qe.onrender.com/](https://automailer-k0qe.onrender.com/)** 
## Features
- Send emails with plain text body and attachments.
- Upload multiple files as attachments.
- Built with Flask and uses a simple SMTP setup for Gmail.

## Requirements
- Python 3.x
- Flask
- smtplib
- email.mime
  
## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/AaronKurian/AutoMailer.git
    cd AutoMailer
    ```

2. Set up a virtual environment (optional but recommended):

    ```bash
    python3 -m venv myenv
    source myenv/bin/activate  # On Windows: myenv\Scripts\activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Access the app at `http://127.0.0.1:8080` (or `http://<your-ip>:8080`).

3. The home page will allow you to:
   - Enter the sender's email and password.
   - Specify recipients (separate with commas).
   - Add a subject and body for the email.
   - Attach files (optional).
   - Send the email immediately.

## Configuration

- **UPLOAD_FOLDER**: The folder where uploaded files are temporarily stored. Default is `'uploads/'`.

## Deployment

1. If deploying on a platform like Render, make sure to specify port `8080` as required by the platform:

    ```bash
    app.run(host='0.0.0.0', port=8080)
    ```

## Notes
- This app uses Gmail's SMTP server (`smtp.gmail.com`) to send emails. You may need to enable "Less secure apps" in your Gmail account settings or use an App Password if Two-Factor Authentication (2FA) is enabled.
- Ensure that the required Python packages are installed as per the `requirements.txt` file.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Made With ❤️ by Aaron Kurian Abraham
