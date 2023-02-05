from flask import Flask, render_template, request, make_response, jsonify
from flask_cors import CORS
from main import response_from_user

app = Flask(__name__)
CORS(app)

@app.route('/')
@app.route('/index.html')
def render_form():
    return render_template('Form.html')

# flask should populate the variable request.form with the user's input in the form.html
@app.route('/data', methods=['POST'])
def user_input():
    print(request.form)
    speed = request.form['speed']
    trip = request.form['trip_len']
    car_type = request.form['car_type']
    grade = request.form['grade']
    resp = make_response()
    resp.status_code = 200
    resp = {"speed" : speed, "trip" : trip, "car_type": car_type, "grade" : grade}
    return jsonify(resp)

# simple API which allows user input to be carried on to ERoute API
@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = response_from_user(text)
    msg = {"answer": response}
    return jsonify(msg)

if __name__ == "__main__":
    app.run(debug=True)