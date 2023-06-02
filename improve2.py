### Flask application used for Improvement
from flask import Flask, request
from transformers import AutoTokenizer, AutoModelForSequenceClassification

from transformers import pipeline
### Change the file path to the new model
classifier = pipeline("sentiment-analysis", model="/content/drive/MyDrive/NCRI/M5")

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