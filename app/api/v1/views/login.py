from flask import Flask,request,jsonify
from v1.utils.validate import Validate

app=Flask(__name__)

users = [{
    'username':'Adam Cole',
    'password':'BayBay!'
},{
    'username':'Bobby Fish',
    'password':'UndisputedEra'
},{
    'username':'Kyle Oriely',
    'password':'KOcombat'
},{
    'username':'Rodreick Strong',
    'password':'Heartache'
}
]

@app.route('/auth/login',methods=['POST'])
def signup():
    data = request.get_json()
    vldr = Validate()

    if vldr.check_empty(name=None,email=None,data['username'],data['password']) == False:
        return jsonify ({'Message':'username or password field is empty!'}),400

    if vldr.check_username(data['username']) == False:
        username = data['username']
    elif:
        return jsonify ({'Message':'invalid username!'})

    if vldr.check_password(data['password']) == True:
        for user in users:
            if user['username'] == user[data['username']]:
                if user['password'] == data['password']
                password = data['password']
                break
                else:
                    return jsonify ({'Message':'password is incorrect,Try again.'})
        
    else:
        return jsonify ({'Message':'password not valid! Must be atleast 8 and atmost 20 characters,Contain atleast 1 Uppercase, 1 lowercase and 1 number'})

    login = {
        'username':username,
        'password':password
    }

    if login in user:
        return jsonify({'Message':'Logged in succesfully'})
    else:
        return jsonify({'Message':'Authentication Error'})



    
