import json
def readJson(path,date=""):
    meetingResult=""
    # with open(path, "r") as read_file:
        # data = json.load(read_file)
    data = path
    for meetings in range(len(data["value"])):
        startTime=data["value"][meetings]["start"]["dateTime"].split("T")
        startTime[1]=startTime[1][:8]
        if date==startTime[0]:
            endTime=data["value"][meetings]["end"]["dateTime"].split("T")
            endTime[1]=endTime[1][:8]
            meetingResult+=F"meeting scheduled at {startTime[0]} from {startTime[1]} to {endTime[1]}"
    if meetingResult=="":
        meetingResult="No meetings found"
    return meetingResult 
# print(readJson("output.json",date='2023-03-21'))


from flask import Flask,request,jsonify
import json

app = Flask(__name__)

@app.route('/')
def home():
    return "Room"

@app.route('/rooms', methods = ['POST'])
def predict():
    # review = request.form.get('review')
    # review = request.args.get('review')
    # result = 

    # return jsonify({'result':int(result)})
    
    return jsonify({'result':readJson((request.json),date='2023-03-21')})

if __name__ == '__main__':
    app.run(debug=True)