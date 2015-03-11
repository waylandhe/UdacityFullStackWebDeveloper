from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
# Hidden! Sign in to twilio.com to find your sid and token
account_sid = ""
auth_token  = ""
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Hi Wayland! You just made your first program to text your phone!",
    to="+14152167239",    # Replace with your phone number
    from_="+14159064184") # Replace with your Twilio number
print message.sid