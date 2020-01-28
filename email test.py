import smtplib
from email.mime.multipart import MIMEMultipart
msg = MIMEMultipart()

msg['Subject'] = "Hello from python"
msg['From'] = 'andrewtalbotprogramming@gmail.com'
msg['To'] = 'andrewtalbotprogramming@gmail.com'

s = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)
password = input('')
s.login('andrewtalbotprogramming@gmail.com',password)

s.send_message(msg)
s.quit()