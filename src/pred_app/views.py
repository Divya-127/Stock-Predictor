import base64
from django.shortcuts import render, redirect
from pred_app.lstm_prediction import *

# --------------- MAIN WEB PAGES -----------------------------
def redirect_root(request):
    return redirect('/pred_app/index')

def index(request):
	return render(request, 'pred_app/index.html') 

def pred(request):
    return render(request, 'pred_app/prediction.html')

def contact(request):
	return render(request, 'pred_app/contact.html')

def search(request, se, stock_symbol):
	import json
	predicted_result_df = lstm_prediction(se, stock_symbol)
	with open('plot.png', "rb") as image_file:
		image_data = base64.b64encode(image_file.read()).decode('utf-8')
	return render(request, 'pred_app/search.html', {"predicted_result_df": predicted_result_df, "image":image_data})
# -----------------------------------------------------------