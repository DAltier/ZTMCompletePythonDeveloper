from twilio.rest import Client

account_sid = 'id'
auth_token = 'secret'
client = Client(account_sid, auth_token)

message = client.messages.create(
         # media_url=['https://images.unsplash.com/photo-1545093149-618ce3bcf49d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=668&q=80'],
         from_='whatsapp:+xxxxxxxxxx',
         body="Hello there. This is your bot: JARVIS, reporting on duty!",
         to='whatsapp:+xxxxxxxxxx'
         )

print(message.sid)