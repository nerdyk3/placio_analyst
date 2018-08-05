from django.shortcuts import render, redirect,HttpResponse
from .models import csvimport
from .forms import DataForm , PlotForm
import pandas as pd
import pdb
from django.template import Context, Template
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
			return render(request,'placio_month/success.html',{'y':KeyCSV})
	else:
		x = DataForm()
		return render(request, 'placio_month/index.html',{'x':x})

def graph(request):
	#pdb.set_trace()
	if request.method == "POST":
		MaP=PlotForm(request.POST)
		if MaP.is_valid():
			#X_axis = MaP.save(commit=False)
			X = MaP.x_axis
			Hue = MaP.hue
			return render(request,'placio_month/graph.html',{"X":Hue})
	else:
		MaP = PlotForm()
		return render(request,'placio_month/success.html',{'MaP':MaP})
