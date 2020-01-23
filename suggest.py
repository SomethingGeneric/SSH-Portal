import os

from emc import mailer
with open("../pass") as f:
    passw = f.read()
m = mailer("mcompton2002@gmail.com",passw)

n = input("Your name (or nickname, I don't judge): ")
c = input("Some form of contact info, if I want to follow up (optional): ")
s = input("Your suggestion, " + n + ": ")

sgst = "From: " + n + "\nContact info: " + c + "\nSuggestion: " + s 

m.mkmessage("3019745990@vtext.com","Suggestion from " + name,sgst)

with open("suggestions.txt","a+") as f:
    f.write(sgst + "\n")

print("Thanks, " + n + "!")
input("Press enter to return")