from emc import mailer
with open("../pass") as f:
    passw = f.read()
m = mailer("mcompton2002@gmail.com",passw)
replyto = input("Email for Matt to respond to: ")
rsubject = input("Subject: ")
rbody = input("Message: ")

subject = "Question from " + replyto
body = "Reply to " + replyto + "\n Subj: " + rsubject + "\n----\n" + rbody

m.mkmessage("3019745990@vtext.com",subject,body)
m.send()
print("Thanks! Sent your question. You'll get a reply to " + replyto)
input("Press enter to return")