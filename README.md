# Fake News Detecton API

#flask #ml #api #sklearn #passiveaggressiveclassifier

This project is a simple fake news detecton application
built as a RESTful api.

The model was trained on [Fake and real news dataset | Kaggle](https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset) with the [Passive Aggressive Classifiers - GeeksforGeeks](https://www.geeksforgeeks.org/passive-aggressive-classifiers/#:~:text=The%20Passive%2DAggressive%20algorithms%20are,even%20intermediate%20Machine%20Learning%20enthusiasts.&text=We%20can%20simply%20say%20that,then%20throw%20away%20the%20example.), an online training algorithm that learns from data fed sequentially to it.

## setup
	#create virual env in project dir
	$python -m venv fake-env

	#activate environment
	$python fake-env/bin/activate

	#install dependencies
	$pip install -r requirements.txt
	
	#start app
	$FLASK_APP=api.py FLASK_ENV=development flask run --port 5000
