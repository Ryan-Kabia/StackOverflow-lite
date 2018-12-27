from flask import Flask,request,jsonify

app=Flask(__name__)

questions = [{
    'author':'Adam Cole',
    'questionId':'001',
    'question':'I,m Adam freaking Cole BayBay! and that is undisputed!',
    'answers':[]
},{
    'author':'Ciampa',
    'questionId':'002',
    'question':'I ended the fairytale! baddest sob on the planet.Follow my lead!',
    'answers':[]
},{
    'author':'Alesiter Black',
    'questionId':'003',
    'question':'You will be absolved of your sins as you fade to black!',
    'answers':[]
},{
    'author':'EC3',
    'questionId':'004',
    'question':'I,m the best here, i am the best there, i am the best anywhere coz im in the top 1 percent.',
    'answers':[]
},{
    'author':'Petee Dunn',
    'questionId':'005',
    'question':'none of the lot could hold a candle to the bruiserweight',
    'answers':[]
},{
    'author':'Velveteen Dream',
    'questionId':'006',
    'question':'Lights! Ambience! Experience! Velveteen Dream!',
    'answers':[]
}]

@app.route('/questions',methods=['GET'])
def fetch_all():
    return jsonify({'Message':questions})

@app.route('/questions/<questionId>',methods=['GET'])
def fetch_specific(questionId):
    for question in questions:
        if question['questionId'] == questionId:
            fetched_item = question
            break
        else:
            fetched_item='Search error, not found!'

    return jsonify({'Message':fetched_item})

@app.route('/questions',methods=['POST'])
def post_question():

    data = request.get_json()

    author = data['author']
    question = data['question']
    questionId = data['questionId']

    post_q = {
        'author':author,
        'question':question,
        'questionId':questionId,
        'answers':[]
    }

    questions.append(post_q)

    return jsonify({'Message':questions})
    
@app.route('/questions/<questionId>',methods=['DELETE'])
def delete_specific(questionId):
    for question in questions:
        if question['questionId'] == questionId:
            questions.remove(question)
            delete_item = questions
            break
        else:
            delete_item = 'Error,Entry not found'
    return jsonify({'Message':delete_item})

@app.route('/questions/<questionId>/answers',methods=['POST'])
def post_answer(questionId):

    data = request.get_json()

    ans_author = data['ans_author']
    answer = data['answer']
    answerId = data['answerId']

    post_a ={
        'ans_author':ans_author,
        'answer':answer,
        'answerId':answerId
    }

    for question in questions:
        if question['questionId'] == questionId:
            question['answers'].append(post_a)
            answered_item = question
            break
        else:
            answered_item='Search error,question not found!'

    return jsonify({'Message':answered_item})



    
