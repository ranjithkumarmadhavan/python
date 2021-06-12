import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from_address = ''
to_address = [""]
message = MIMEMultipart()
message['From'] = from_address
message['To'] = " ,".join(to_address)
message['subject'] = 'Hello from smtp'

body = "Hello Ranjith"

message.attach(MIMEText(body,'plain'))

email = ""
password = ""

mail = smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.ehlo()
mail.login(email,password)
text = message.as_string()
mail.sendmail(from_address,to_address,text)
mail.quit()