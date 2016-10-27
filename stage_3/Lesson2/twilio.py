#from twilio, an external python library, import the rest folder. 
from twilio import rest

account_sid = "{{ #private info }}" # Your Account SID from www.twilio.com/console
auth_token  = "{{ #private info }}"  # Your Auth Token from www.twilio.com/console

#Inside the rest folder is a class called TwilioRestClient.
#rest.TwilioRestClient will call the init function defined in the class which creates an instance called client. 
client = rest.TwilioRestClient(account_sid, auth_token)

#Now we can do things defined in class TwilioRestClient, such as connecting with Twilio to send a text message. 
message = client.messages.create(body="Hey! You might be the next Customer Success Advocate!",
    to="",    # Replace with your phone number
    from_="+19099067001") # My Twilio number

print(message.sid)
