from v1.views.questions import app
from v1.models.database import *
from flask import json

data1 ={
        "username":"Fishbone",
        "password":"1Fishyboi",
        "question":"What is undisputed and all the gold?",
        "questionId":"001",
        }

data2 ={
        "username":"Fishbone1",
        "password":"1Fishyboi",
        "question":"",
        "questionId":"001",
        }

data3 ={
        "username":"Fishbone1",
        "password":"1Fishyboi",
        "question":"What is undisputed and all the gold?",
        "questionId":"007",
        }

data4 ={
        "username":"Fishbone1",
        "password":"1Fishyboy",
        }

data5 ={
        "username":"Fishbone1",
        "password":"1Fishyboi",
        }

data6 ={
        "username":"Fishbone1",
        "password":"1Fishyboi",
        "answer":"",
        "answerId":"",
        }

data7 ={
        "username":"Fishbone1",
        "password":"1Fishyboi",
        "answer":"We run this place!,and that is undisputed!",
        "answerId":"002",
        }


def test_g_all_questions():
    response = app.test_client().get('/questions',content_type='application/json',)

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data['All Questions'] == post_qstns

def test_g_specific_questions():
    count = len(post_qstns)
    for i in range(1,(count+1)):
        response = app.test_client().get('/questions/00{}'.format(i),content_type='application/json',)

        data = json.loads(response.get_data(as_text=True))

        assert response.status_code == 200
        assert data["Search Results"] == post_qstns[(i-1)]

def test_p_failed_login():
    response = app.test_client().post('/questions',data = json.dumps(data1),content_type='application/json',)

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 401
    assert data["Message"] == "login unsuccessful,invalid username or password"

def test_p_empty_field():
    response = app.test_client().post('/questions',data = json.dumps(data2),content_type='application/json',)

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 400
    assert data["Message"] == "question or questionId fields are empty!"

def test_p_post_succesful():
    response = app.test_client().post('/questions',data = json.dumps(data3),content_type='application/json',)

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data["Message"] == "QID 007(Fishbone1): What is undisputed and all the gold?"

def test_d_failed_login():
    count = len(post_qstns)
    for i in range(1,(count+1)):
        response = app.test_client().delete('/questions/00{}'.format(i),data = json.dumps(data4),content_type='application/json',)

        data = json.loads(response.get_data(as_text=True))

        assert response.status_code == 401
        assert data["Message"] == "login unsuccessful,invalid username or password"

def test_d_question_not_found():
    no_exist = len(post_qstns)+1

    response = app.test_client().delete('/questions/00{}'.format(no_exist),data = json.dumps(data5),content_type='application/json',)

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 400
    assert data["Message"] == "Error,questionId could not be found"

def test_d_restricted():
    cant = []
    for query in post_qstns:
        if query["author"] != data5["username"]:
            cant.append(query["questionId"])

    for i in (cant):
        response = app.test_client().delete('/questions/{}'.format(i),data = json.dumps(data5),content_type='application/json',)

        data = json.loads(response.get_data(as_text=True))

        assert response.status_code == 401
        assert data["Message"] == "Only the author of the question can delete it"

def test_d_succesful():
    can = []
    for query in post_qstns:
        if query["author"] == data5["username"]:
            can.append(query["questionId"])

    for i in (can):
        response = app.test_client().delete('/questions/{}'.format(i),data = json.dumps(data5),content_type='application/json',)

        data = json.loads(response.get_data(as_text=True))

        assert response.status_code == 200
        assert data["Message"] == "question (ID {}) was deleted succesfully".format(i)

def test_p_answer_failed_login():
    count = len(post_qstns)
    for i in range(1,(count+1)):
        response = app.test_client().post('/questions/00{}/answers'.format(i),data = json.dumps(data4),content_type='application/json',)

        data = json.loads(response.get_data(as_text=True))

        assert response.status_code == 401
        assert data["Message"] == "login unsuccessful,invalid username or password"

def test_p_answer_empty_field():
    count = len(post_qstns)
    for i in range(1,(count+1)):
        response = app.test_client().post('/questions/00{}/answers'.format(i),data = json.dumps(data6),content_type='application/json',)

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 400
    assert data["Message"] == "answer or answerId fields are empty!"




    
