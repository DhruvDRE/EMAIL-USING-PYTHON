# for succesfully sending the email kindly go to google account and allow access to less secure app settings
import smtplib
#email constraints
sender="" # your personal mail id
recipient="" # to the email address you want to send
subject="I sent email through python code"
message="Hi this is dhruv ,\n\n i am soo happy to send this email through automation python code"

# format of email
email="Subject: {}\n\n{}".format(subject,message)

#senders email pass - personal id
psd_file=open("gmailpass.txt","r")
pas=psd_file.readline()
psd_file.close()

# create STMP session for user
s=smtplib.SMTP("smtp.gmail.com",587) # its unique session id
s.ehlo()
# start TLS for transport layer ,secures credentials
s.starttls()
s.login(sender,pas)
#authentication
s.sendmail(sender,recipient,email)

# terminate the session
s.quit()

#success mmsg
print("\nSuccessfully sent to recipient")
