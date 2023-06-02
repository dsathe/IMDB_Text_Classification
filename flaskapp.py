### Flask application used for benchmarking 
from flask import Flask, json, request, Response, jsonify, render_template   
from transformers import AutoTokenizer, AutoModelForSequenceClassification

from transformers import pipeline

#### Just change the path to the saved model
classifier = pipeline("sentiment-analysis", model="D:\AA_USC\CSCI_571_WT\Homework6\Flask_Project\M3")

app = Flask(__name__)


@app.route('/analysis')
def analysis():
    try:
        df=classifier(request.args.get('jsonobj'))
        return df[0]['label']
    except:
        return "HTTP Error"
    


if __name__ == "__main__":
    app.run()