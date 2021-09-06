from flask import Flask, jsonify, request, make_response, json
from prediction_model import PredictionModel
import pandas as pd
from flask_cors import CORS
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

app.config['SECRET_KEY'] = '4c99e0361905b9f941f17729187afdb9'

CORS = CORS(app, resources={r"/api*": {"origins": "*"}})

# @app.before_request
# def log_request_info():
#     app.logger.debug('Headers: %s', request.headers)
#     app.logger.debug('Body: %s', request.data)

@app.route("/api", methods=['GET'])
def api():
	request_data = request.data
	if request_data != "" and len(str(request_data)) > 10:
		model = PredictionModel(str(request_data))
		res = model.predict()
		return make_response(res)
	else: return jsonify(error=400, message=str("No body text passed to model or Text too short")), 400
	

@app.route('/predict/<original_text>', methods=['POST', 'GET'])
def predict(original_text):
	model = PredictionModel(original_text)
	return jsonify(model.predict())

# @app.errorhandler(e)
# def handle_exception(e):

@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "message": e.description,
    })
    response.content_type = "application/json"
    return response

if __name__ == '__main__':
	app.run(port=5000)
