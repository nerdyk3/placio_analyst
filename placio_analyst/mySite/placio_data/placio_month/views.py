from django.shortcuts import render, redirect
from .models import csvimport
from .forms import DataForm , PlotForm
import pandas as pd
#import seaborn as sys

# Create your views here.

def index(request):
	if request.method == "POST":
		x = DataForm(request.POST, request.FILES)
		if x.is_valid():
			data = x.save(commit=False)
			#data.save()
			FileRead = data.file
			ReadCSV = pd.read_csv(FileRead)
			KeyCSV = ReadCSV.keys()
			return redirect('graph',y=KeyCSV)
	else:
		x = DataForm()
	return render(request, 'placio_month/index.html',{'x':x})

def graph(request):
	if request.method == "POST":
		MaP=PlotForm(request.POST)
		if MaP.is_valid():
			#X_axis = MaP.save(commit=False)
			X = MaP.x_axis
			Hue = MaP.hue
			data=[{'X':X}]
			return render(request,'placio_month/graph.html', data)
	else:
		MaP = PlotForm()
	return render(request,'placio_month/success.html',[{'MaP':MaP},{'y':y}])