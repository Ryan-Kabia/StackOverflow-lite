
from flask import Flask,request,jsonify

app=Flask(__name__)

questions = [{
    'author':'Adam Cole',
    'question_id':'001',
    'question':'I,m Adam freaking Cole BayBay! and that is undisputed!'
},{
    'author':'Ciampa',
    'question_id':'002',
    'question':'I ended the fairytale! baddest sob on the planet.Follow my lead!'
},{
    'author':'Alesiter Black',
    'question_id':'003',
    'question':'You will be absolved of your sins as you fade to black!'
},{
    'author':'EC3',
    'question_id':'004',
    'question':'I,m the best here, i am the best thier, i am the best anywhere coz im in the top 1 percent.'
},{
    'author':'Petee Dunn',
    'question_id':'005',
    'question':'none of the lot could hold a candle to the bruiserweight'
},{
    'author':'Velveteen Dream',
    'question_id':'006',
    'question':'Lights! Ambience! Experience! Velveteen Dream!'
}
]

@app.route('/questions',methods=['GET'])
def fetch_all():
    return jsonify({'Message':questions})



    




    
