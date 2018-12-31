from flask import Flask,request,jsonify
from v1.utils.validate import Validate, SimulateLogin
from v1.models.database import *


app=Flask(__name__)

@app.route("/questions",methods=["GET"])
def fetch_all():
    return jsonify({"All Questions":post_qstns}),200

@app.route("/questions/<questionId>",methods=["GET"])
def fetch_specific(questionId):
    for question in post_qstns:
        if question["questionId"] == questionId:
            fetched_item = question
            return jsonify({"Search Results":fetched_item}),200
            break
        else:
            return jsonify ({"Message":"Question not found"}),404

    

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
        return jsonify ({"Message":"login unsuccessful,invalid username or password"}),200

    vldr = Validate()

    if vldr.check_empty_question(data["question"],data["questionId"]) == False:
        return jsonify ({"Message":"question or questionId fields are empty!"}),400
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

    return jsonify({"Message":"QID {}({}): {}".format(post_q['questionId'],post_q['author'],post_q['question'])}),200
    
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
        return jsonify ({"Message":"login unsuccessful,invalid username or password"}),401

    for question in post_qstns:
        query = question
        
        if query["questionId"] == questionId:
            if query["author"] == current_user["username"]:
                post_qstns.remove(question)
                delete_item = post_qstns
                return jsonify ({"Message":"question (ID {}) was deleted succesfully".format(questionId)}),200
                break
            else:
                return jsonify ({"Message":"Only the author of the question can delete it"}),401
        else:
            return jsonify ({"Message":"Error,questionId could not be found"})
    
@app.route("/questions/<questionId>/answers",methods=["POST"])
def post_answer(questionId):

    data = request.get_json()
    #Placeholder function for auth using tokens
    sim_user = SimulateLogin
    
    if sim_user.sim(data["username"], data["password"]) == True:
        current_user = {"username":data["username"],
                        "password":data["password"]
                        }
    else:
        return jsonify ({"Message":"login unsuccessful,invalid username or password"}),401

    vldr = Validate()

    if vldr.check_empty_question(data["answer"],data["answerId"]) == False:
        return jsonify ({"Message":"answer or answerId fields are empty!"}),400
    else:
        ans_author = current_user["username"]
        answer = data["answer"]
        answerId = data["answerId"]

    
    post_a ={
        "ans_author":ans_author,
        "answer":answer,
        "answerId":answerId
    }

    for question in post_qstns:
        query = question
        ans_to_qstn = []
        if query["questionId"] == questionId:
            post_a.update(questionId = questionId)
            post_ans.append(post_a)
            for answer in post_ans:
                ans_query = answer
                if ans_query["questionId"] == questionId:
                    ans_to_qstn.append(ans_query)

            return jsonify({"Question":"Q-ID({}):{}".format(questionId,query["question"])},{"Answer":"A-ID({}):{}".format(post_a["questionId"],post_a["answer"])},{"All Answers to this question":ans_to_qstn}),200
            break
        else:
           return jsonify ({"Message":"Error,question could not be found"}),404

    

    


    
