from flask import Flask,jsonify,request
app = Flask(__name__)
phones = [
    {
        'contact': '9987644456',
        'name': "Raju",
        "done": False,
        "id":1
    },
    {
        'contact': '9876543222',
        'name': "Rahul",
        "done": False,
        "id":2
    }
]

@app.route("/add-data", method=["POST"])

def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide data"
        },400)
    contact = {
        'id': phones[-1]['id']+1,
        'name': request.json['name'],
        'contact': request.json.get('contact', ""),
        'done': False
    }
    phones.append(contact)
    return jsonify({
        'status':'success',
        'message':"task is completed"
    })
@app.route('/get-data')
def get_task():
    return jsonify({
        'data':phones,
    })
if(__name__=="__name__"):
    app.run(debug=True)