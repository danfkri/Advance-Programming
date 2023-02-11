import smtplib

class Email:
	
	subject = 'CSV copy by Python'
	body = 'Copy completed'
	sender = ''
	receiver = ''
	password = ''
	
	message = 'subject: ' + subject+'\n\n' + body
	
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(sender, password)
	server.sendmail(sender, receiver, message)
