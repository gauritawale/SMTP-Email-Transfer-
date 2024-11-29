import smtplib

# Establish connection with the SMTP server
s = smtplib.SMTP("smtp.gmail.com", 587)
s.starttls()

# Login credentials
s.login('gauritawale04@gmail.com', 'seny kjqt osjk pjfx')

# Define the email components
subject = "Greetings"
body = "Hi Gauri,\n\nThis is a test email sent using Python.\n\nRegards,\nYour Name"
message = f"Subject: {subject}\n\n{body}"

# Send the email
s.sendmail('gauritawale04@gmail.com', 'gauritawale04@gmail.com', message)

# Close the connection
s.quit()
