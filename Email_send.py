from email.message import EmailMessage
import smtplib
import ssl

def send_email():
    # Prompt user for sender credentials and recipient details
    email_sender = input("Enter your email: ")
    email_password = input("Enter your email password (use app password if required): ")
    email_receiver = input("Enter the receiver's email: ")
    
    # Collect subject and body of the email
    subject = input("Subject: ")
    body = input("Body: ")

    # Initialize email message
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = email_sender
    msg['To'] = email_receiver
    msg.set_content(body)

    try:
        # Securely send the email
        context = ssl.create_default_context()  # Create SSL context for secure connection
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)  # Login to the sender's email account
            smtp.send_message(msg)  # Send the email
            print("Email sent successfully!")
    except smtplib.SMTPAuthenticationError:
        print("Authentication error. Please check your email or password.")
    except smtplib.SMTPException as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    send_email()
