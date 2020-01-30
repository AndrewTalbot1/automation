import requests
import smtplib
from email.message import EmailMessage

with open("listurls.txt", "w") as f:       
    f.truncate(0)                           
with open ("testurls.txt", "r") as txt_file:
    for urls in txt_file:
        request = requests.get(urls)
        try:
            request.raise_for_status()
        except Exception as error:
            error = 'There was a problem: %s' % (error)

            with open("listurls.txt", "a") as f:       #Opens file so I can loop through and append the results
                f.writelines(error+ "\n")               #Writes the new data to the file in seperated lines
        else:
            pass
with open("listurls.txt", "r") as file_to_send:
    msg = EmailMessage()
    msg.set_content(file_to_send.read())

msg['Subject'] = "Here are the list of URLs that don't work"
msg['From'] = 'andrewtalbotprogramming@gmail.com'
msg['To'] = 'andrewtalbotprogramming@gmail.com'

s = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)
print("Enter Your Password To Continue")
password = input('')
s.login('andrewtalbotprogramming@gmail.com',password)

s.send_message(msg)
s.quit()
