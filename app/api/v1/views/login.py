from flask import Flask,request,jsonify

app=Flask(__name__)

user = [{
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

    username = data['username']
    password = data['password']

    login = {
        'username':username,
        'password':password
    }

    if login in user:
        return jsonify({'Message':'Logged in succesfully'})
    else:
        return jsonify({'Message':'Authentication Error'})



    
