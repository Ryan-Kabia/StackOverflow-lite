from flask import jsonify
import re

class Validate():

    def check_empty(self,name,email,username,password):

       if name == "" or email == "" or username == "" or password == "":
           return False

    def check_username(self,username):
        registered_users = []

        if username in registered_users:
            return False

        elif username not in registered_users:
            registered_users.append(username)
            return True
        
    def valid_email(self,email):
        vemail = re.compile(r'(\w+[.|\w])*@(\w+[.])*\w+') 

        if not vemail.match(email):
            return False
        else:
            return True
    def check_email(self,email):
        registered_emails = []

        if email not in registered_emails:
            registered_emails.append(email)
            return True
        elif email in registered_emails:
            return False
        
    def check_password(self,password):
        pswd = password

        if (len(pswd)<8):
            return False
        elif (len(pswd)>20):
            return False
        elif not re.search("[A-Z]",pswd):
            return False
        elif not re.search("[a-z]",pswd):
            return False
        elif not re.search("[0-9]",pswd):
            return False
        else:
            return True