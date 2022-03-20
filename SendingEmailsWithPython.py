import smtplib

sender_email = input(str("Please Enter your email address: "))
password = input(str("Please enter your password: "))
receiver_email = input(str("Enter receiver's email address: "))
message = input(str("Write your message: "))

server = smtplib.SMTP('smtp.gmail.com',587)

server.starttls()

server.login(sender_email, password)
print('login success !!')
server.sendmail(sender_email, receiver_email, message)
print("Message is sent!")