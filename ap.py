from flask import Flask,jsonify,request
app = Flask(__name__)
tasks = [
    {
        "id":1,
        "title":"buy grocery",
        "description":["milk","rice"],
        "done":False
    },
     {
        "id":2,
        "title":"reading",
        "description":["english","maths"],
        "done":False
    },
]
@app.route("/")
def hello():
    return "welcome"

@app.route("/get-data")
def bye():
    return jsonify({
        "data" : tasks
    })

@app.route("/add-data",methods=["POST"])
def good():
    if not request.json:
        return jsonify({
            "message":"please enter information"
        })
    i = {
        "id":tasks[-1]["id"]+1,
         "title": request.json["title"],
        "description":request.json["description"],
        "done":False
    }
    tasks.append(i)
    return jsonify({
        "message":"task added succesfully"
    })

if(__name__=="__main__"):
    app.run()