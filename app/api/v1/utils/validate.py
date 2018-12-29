from flask import Flask

app = Flask[__name__]

Class Valitdate():
    def check_username(new_user):
        registered_users = []

        if new_user('username') not in registered_users:
            registered_users.append(new_user('username'))
            return True
        elif new_user('username') in registered_users:
            return ({'Message':'username already taken!'})

    def check_email(new_user):
        valid_email = re.compile(r'(\w+[.|\w])*@(\w+[.])*\w+') 
        registered_emails = []

        if valid_email.match(new_user('email')):
            if new_user('email') not in registered_emails:
                registered_emails.append(new_user('email'))
                return True
            elif new_user('email') in registered_emails:
                return ({'Message':'email already taken!'})
        elif not valid_email.match(new_user('email')):
            return ({'Message':'email is not valid!'})

    def check_password(new_user):
        pswd = new_user('password')

        if (len(pswd)<8):
            return ({'Message':'Password is too short.Minimum of 8 charaters'})
        elif (len(pswd)>20):
            return ({'Message':'Password is too long.Maximum of 20 charaters'})
        elif not re.search("[A-Z]",pswd):
            return ({'Message':'Password should contain atleast 1 uppercase letter'})
        elif not re.search("[a-z]",pswd):
            return ({'Message':'Password should contain atleast 1 lowercase letter'})
        elif not re.search("[0-9]",pswd):
            return ({'Message':'Password should contain atleast 1 number'})
        else:
            return True