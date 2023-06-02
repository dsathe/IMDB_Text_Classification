# IMDB_Text_Classification
Use Hugging Face to create Text Classification model and perform benchmarking on the model
We use "Bert base uncased model" as our pretrained model

## Part 1
We fine tune the original model on our IMDB dataset by training it for 3 epochs. This is given in train.ipynb.

## Part 2
We use the saved trained model and create a flask application. We run the flask application on the jupyter notebook itself by running it in background.
We make use of flaskapp.py script for running the code in background.
Finally to perform benchmarking make calls to the flask application using 10050 different examples and find out the time required by Bert base uncased model.
This is done in benchmark.ipynb.

## Part 3
Now we create a new model using the distilbert base uncased. Train it the same way for 3 epochs improved_model.ipynb

## Part 4
As done in Part 4 we make use for the newly improved trained model and create a new flask application. We use improve2.py to create it in background in the jupyter nodebook. 
Finally check how much time it takes for the newly trained model using the same examples and find out what time is required by Distil bert based uncased.

## Observations
Distill Bert model has a better performance than bert base model as it is lighter than current bert model.
It has near about same accuracy as the bert base model
