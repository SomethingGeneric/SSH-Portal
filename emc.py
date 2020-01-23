import os,sys,getpass
from gmail import *

class mailer:
        def __init__(self,fromad,password):
            self.e = GMail(fromad,password)
        def mkmessage(self,to,subject,body):
            self.m = Message(subject,to=to,text=body)
        def send(self):
            self.e.send(self.m)
