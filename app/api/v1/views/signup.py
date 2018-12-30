from flask import Flask,request,jsonify
from v1.utils.validate import Validate
app = Flask (__name__)

user = []

@app.route('/auth/signup',methods=['POST'])
def signup():
    data = request.get_json()
    vldr = Validate()

    if vldr.check_empty(data['name'],data['email'],data['username'],data['password']) == False:
        return jsonify ({'Message':'name,email,username or password fields are empty!'}),400
    else:
        name = data['name']

    if vldr.check_username(data['username']) == True:
        username = data['username']
    else:
        return jsonify ({'Message':'username is already taken'})

    if vldr.valid_email(data['email']) == True:
        if vldr.check_email(data['email']) == True:
            email = data['email']
        else:
            return jsonify ({'Message':'email already in use,choose a diffrent one'})
    else:
        return jsonify ({'Message':'email is not valid!'})

    if vldr.check_password(data['password']) == True:
        password = data['password']
    else:
        return jsonify ({'Message':'password not valid! Must be atleast 8 and atmost 20 characters,Contain atleast 1 Uppercase, 1 lowercase and 1 number'})

    try:
        if not data:
            return jsonify({'Message':'Data not found'}),400
        
            return jsonify({'message':'name,email,username or password fields are empty!'}),400
    except:
        return jsonify ({'Message':'name,email,username or password fields missing'})

    new_user = {
        'name':name,
        'email':email,
        'username':username,
        'password':password
    }

    user.append(new_user)
    return jsonify({'Message':'{} added succesfully'.format(new_user['username'])})
