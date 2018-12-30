from v1.models.database import reg_users
from flask import jsonify
import re

class Validate():

    def check_empty(self,name,email,username,password):

       if name == "" or email == "" or username == "" or password == "":
           return False

    def check_username(self,username):
        rusers = []
        for user in reg_users:
            plc_hld = user['username']
            rusers.append(plc_hld)

        if username in rusers:
            return False

        elif username not in rusers:
            return True
        
    def valid_email(self,email):
        vemail = re.compile(r'(\w+[.|\w])*@(\w+[.])*\w+') 

        if not vemail.match(email):
            return False
        else:
            return True
    def check_email(self,email):
        remails = []

        for user in reg_users:
            plc_hld = user['email']
            remails.append(plc_hld)

        if email in remails:
            return False

        elif email not in remails:
            return True
        
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

    def valid_password(self,password,username):
        
        rusers = []
        for user in reg_users:
            plc_hld = user

            if plc_hld['username'] == username:
                if plc_hld['password'] == password:
                    return True 
                    break   
                else:
                    return False