from emc import mailer
m = mailer("mcompton2002@gmail.com","Igothacked?21")
replyto = input("Email for Matt to respond to: ")
rsubject = input("Subject: ")
rbody = input("Message: ")

subject = "Question from " + replyto
body = "Reply to " + replyto + "\n Subj: " + rsubject + "\n----\n" + rbody

m.mkmessage("3019745990@vtext.com",subject,body)
m.send()
print("Thanks! Sent your question. You'll get a reply to " + replyto)
