from flask import Flask,request,jsonify

app=Flask(__name__)

user = []

@app.route('/auth/signup',methods=['POST'])
def signup():
    data = request.get_json()

    name = data['name']
    email = data['email']
    username = data['username']
    password = data['password']

    new_user = {
        'name':name,
        'email':email,
        'username':username,
        'password':password
    }

    user.append(new_user)
    return jsonify({'Message':'New user added succesfully'})
