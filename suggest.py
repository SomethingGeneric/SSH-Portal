import os

n = input("Your name (or nickname, I don't judge): ")
c = input("Some form of contact info, if I want to follow up (optional): ")
s = input("Your suggestion, " + n + ": ")

sgst = "From: " + n + "\nContact info: " + c + "\nSuggestion: " + s 

with open("suggestions.txt","a+") as f:
    f.write(sgst + "\n")

print("Thanks, " + n + "!")