from flask import Flask,request,jsonify
from v1.utils.validate import Validate
from v1.models.database import reg_users

app=Flask(__name__)

@app.route('/auth/login',methods=['POST'])
def signup():
    data = request.get_json()
    vldr = Validate()

    if vldr.check_empty(name=None,email=None,username=data['username'],password=data['password']) == False:
        return jsonify ({'Message':'username or password field is empty!'}),400

    if vldr.check_username(data['username']) == False:
        username = data['username']
        if vldr.check_password(data['password']) == True:
            if vldr.valid_password(data['password'],data['username']) == True:
                password = data['password']
            else:
                return jsonify ({'Message':'password is incorrect,Try again.'})
        else:
            return jsonify ({'Message':'password not valid! Must be atleast 8 and atmost 20 characters,Contain atleast 1 Uppercase, 1 lowercase and 1 number'})
    else:
        return jsonify ({'Message':'invalid username!'})

   
    logged_user = {
        'username':username,
        'password':password
    }

    if logged_user:
        return jsonify({'Message':'{} logged in succesfully'.format(logged_user['username'])})



    
