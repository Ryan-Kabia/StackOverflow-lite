from flask import Flask,request,jsonify
from v1.utils.validate import Validate, SimulateLogin
from v1.models.database import *


app=Flask(__name__)

@app.route("/questions",methods=["GET"])
def fetch_all():
    return jsonify({"Message":post_qstns})

@app.route("/questions/<questionId>",methods=["GET"])
def fetch_specific(questionId):
    for question in post_qstns:
        if question["questionId"] == questionId:
            fetched_item = question
            break
        else:
            fetched_item="Search error, question not found!"

    return jsonify({"Message":fetched_item})

@app.route("/questions",methods=["POST"])
def post_question():
    data = request.get_json()
    #Placeholder function for auth using tokens
    sim_user = SimulateLogin
    
    if sim_user.sim(data["username"], data["password"]) == True:
        current_user = {"username":data["username"],
                        "password":data["password"]
                        }
    else:
        return jsonify ({"Message":"login unsuccessful,invalid username or password"})

    vldr = Validate()

    if vldr.check_empty_question(data["question"],data["questionId"]) == False:
        return jsonify ({"Message":"author,question or questionId fields are empty!"}),400
    else:
        author = current_user["username"]
        question = data["question"]
        questionId = data["questionId"]

    post_q = {
        "author":author,
        "question":question,
        "questionId":questionId,
    }

    post_qstns.append(post_q)

    return jsonify({"Message":"QID {}({}): {}".format(post_q['questionId'],post_q['author'],post_q['question'])})
    
@app.route("/questions/<questionId>",methods=["DELETE"])
def delete_specific(questionId):
    data = request.get_json()
    #Placeholder function for auth using tokens
    sim_user = SimulateLogin
    
    if sim_user.sim(data["username"], data["password"]) == True:
        current_user = {"username":data["username"],
                        "password":data["password"]
                        }
    else:
        return jsonify ({"Message":"login unsuccessful,invalid username or password"})

    for question in post_qstns:
        query = question
        
        if query["questionId"] == questionId:
            if query["author"] == current_user["username"]:
                post_qstns.remove(question)
                delete_item = post_qstns
                return jsonify ({"Message":"question (ID {}) was deleted succesfully".format(questionId)})
                break
            else:
                return jsonify ({"Message":"Only the author of the question can delete it"})
        else:
            return jsonify ({"Message":"Error,questionId could not be found"})
    
@app.route("/questions/<questionId>/answers",methods=["POST"])
def post_answer(questionId):

    data = request.get_json()
    vldr = Validate()

    if vldr.check_empty_question(data["ans_author"],data["answer"],data["answerId"]) == False:
        return jsonify ({"Message":"ans_author,answer or answerId fields are empty!"}),400
    else:
        ans_author = data["ans_author"]
        answer = data["answer"]
        answerId = data["answerId"]

    
    post_a ={
        "ans_author":ans_author,
        "answer":answer,
        "answerId":answerId
    }

    for question in post_qstns:
        if question["questionId"] == questionId:
            query = question
            post_a.update("questionId",questionId)
            post_ans.append(post_a)
            return jsonify({"Message":"Succesfully Answered {} with {}".format(query["question"],post_a["answer"])})
            break
        else:
           return jsonify ({"Message":"Error,question could not be found"})

    

    


    
