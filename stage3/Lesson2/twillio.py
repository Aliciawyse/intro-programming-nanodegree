#Pythons from statement lets you import specific attributes from a module.
#Inside twilio theres a folder called rest and inside that is a class called twiolio rest client 
#and we're going to use that in our code. 

from twilio.rest import TwilioRestClient

account_sid = "{{  }}" # Your Account SID from www.twilio.com/console
auth_token  = "{{  }}"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="",    # Replace with your phone number
    from_="+19099067001) # Replace with your Twilio number

print(message.sid)
