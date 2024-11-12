from dotenv import load_dotenv
from flask import Flask,request,render_template,jsonify
import os
from crop_recommendation_repo.main import getCropRecommendation,processDataAndGetCropRecommendation

load_dotenv()

app = Flask(__name__)

server_secret_key = os.getenv('SECRET_KEY')

@app.route('/',methods=['GET','POST'])
def index():
    if(request.method == 'POST'):
        prediction = processDataAndGetCropRecommendation(request.form)
        return render_template('home.html',name=prediction[0]) 
    return render_template('form.html')
    

@app.route('/crop-recommendation',methods=['POST'])
def recommend():
    # Get JSON data from the request
    data = request.get_json()
    
    # validate secretKey
    secretKey = data.get('secretKey')
    if secretKey != server_secret_key:
        return jsonify({'error': 'secretKey not matched'}), 400
    
    # Check if the data contains the 'numbers' key
    readings = data.get('cropReadings')
    
    # Ensure the 'readings' is actually a list
    if not isinstance(readings, list):
        return jsonify({'error': 'readings should be a list'}), 400
    
     # Get Crop Recommendation
    recommendation = getCropRecommendation(readings)

    # Return the result as JSON
    return jsonify({'recommendation': recommendation})


if __name__=='__main__':
    app.run(debug=True,port=38000)
    
    
