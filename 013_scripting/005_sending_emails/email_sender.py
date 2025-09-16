import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path    # or os.path

html = Template(Path(r"c:\Users\cnx36\Documents\7.Projects\1.ZeroToMastery\CompletePythonDeveloper\013_scripting\005_sending_emails\index.html").read_text())

email = EmailMessage()
email['from'] = 'Andrei Neagoie'
email['to'] = 'wicked_girl@outlook.com'
email['subject'] = 'You won 1,000,000 dollars!'
email.set_content(html.substitute({'name': 'Andrei'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('zerotomastery1@gmail.com', 'helloztmmyoldfriend1')
	smtp.send_message(email)
	print('all good boss!')