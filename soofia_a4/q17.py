# 17. Install and import suitable package to send SMS on mobile
# importing twilio
from twilio.rest import Client
  
# Your Account Sid and Auth Token from twilio.com / console
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'
  
client = Client(account_sid, auth_token)
  
''' Change the value of 'from' with the number 
received from Twilio and the value of 'to'
with the number in which you want to send message.'''
message = client.messages.create(
                              from_='+15017122661',
                              body ='body',
                              to ='+15558675310'
                          )
  
print(message.sid)