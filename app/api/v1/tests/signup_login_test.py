from v1.views.signup_login import app
from flask import json

data1 ={
        'name':'',
        'email':'',
        'username':'',
        'password':''
        }

data2 = {
        'name':'Lacey',
        'email':'le@nxt',
        'username':'BayBay',
        'password':'Laceyevans123'
        }

data3 = {
        'name':'Lacey',
        'email':'lenxt.com',
        'username':'LaceyE',
        'password':'Laceyevans123'
        }

data4 = {
        'name':'Lacey',
        'email':'kocombat@nx3',
        'username':'LaceyE',
        'password':'Laceyevans123'
        }

data5 = {
        'name':'Lacey',
        'email':'le@nxt',
        'username':'LaceyE',
        'password':'laceyevans'
        }

data6 = {
        'name':'Lacey',
        'email':'le@nxt',
        'username':'laceyE',
        'password':'Laceyevans123'
        }

data7 = {
        "username":"",
        "password":""
        }

data8 = {
        "username":"Fish",
        "password":"1Fishyboi"
        }

data9 = {
        "username":"Fishbone1",
        "password":"Fishyboi"
        }

data10 = {
        "username":"Fishbone1",
        "password":"1Fishybo"
        }

data11 = {
        "username":"Fishbone1",
        "password":"1Fishyboi"
        }

def test_s_empty():
    response = app.test_client().post('/auth/signup',data = json.dumps(data1),content_type='application/json',)

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 400
    assert data['Message'] == "name,email,username or password fields are empty!"

def test_s_taken_username():
    response = app.test_client().post('/auth/signup',data = json.dumps(data2),content_type='application/json',)

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 403
    assert data['Message'] == "username is already taken"

def test_s_invalid_email():
    response = app.test_client().post('/auth/signup',data = json.dumps(data3),content_type='application/json',)

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 400
    assert data['Message'] == "email is not valid!"

def test_s_taken_email():
    response = app.test_client().post('/auth/signup',data = json.dumps(data4),content_type='application/json',)

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 403
    assert data['Message'] == "email already in use,choose a diffrent one"

def test_s_invalid_password():
    response = app.test_client().post('/auth/signup',data = json.dumps(data5),content_type='application/json',)

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 400
    assert data['Message'] == "password not valid! Must be atleast 8 and atmost 20 characters,Contain atleast 1 Uppercase, 1 lowercase and 1 number"

def test_s_successful():
    response = app.test_client().post('/auth/signup',data = json.dumps(data6),content_type='application/json',)

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data['Message'] == "laceyE added succesfully"

def test_l_empty():
    response = app.test_client().post('/auth/login',data = json.dumps(data7),content_type='application/json',)

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 400
    assert data['Message'] == "username or password field is empty!"
    
def test_l_invalid_username():
    response = app.test_client().post('/auth/login',data = json.dumps(data8),content_type='application/json',)

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 401
    assert data['Message'] == "invalid username!"

def test_l_invalid_password():
    response = app.test_client().post('/auth/login',data = json.dumps(data9),content_type='application/json',)

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 400
    assert data['Message'] == "password not valid! Must be atleast 8 and atmost 20 characters,Contain atleast 1 Uppercase, 1 lowercase and 1 number"

def test_l_incorrect_password():
    response = app.test_client().post('/auth/login',data = json.dumps(data10),content_type='application/json',)

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 401
    assert data['Message'] == "password is incorrect,Try again."

def test_l_successful():
    response = app.test_client().post('/auth/login',data = json.dumps(data11),content_type='application/json',)

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data['Message'] == "Fishbone1 logged in succesfully"