import smtplib

from email.message import EmailMessage

#Creating the e-mail function

mail = EmailMessage()

mail["from"] = "Me"

#Inserting the e-mail to send to 

mail["to"] = email_to_send_to

mail["subject"] = "Email sent"

mail.set_content("Email sent via Python code")

#Insert the smtp codes for the different email servers - for Yahoo it's this

with smtplib.SMTP(host="smtp.mail.yahoo.com", port = 587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login(your_email, your_password)
  smtp.send_message(mail)
  #receive confirmation
  print("good")
