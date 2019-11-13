from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import subject


#Is it standard to define libraries here if a view needs it?
import wfdb
import matplotlib.pyplot as plt
import numpy as np
import codecs, json

# Create your views here.

def subject_detail_view(request):
    
    num = request.GET.get('subject') #obtain the value of a GET variable with the name 'subject'
    patient = subject.objects.get(id=num)
    temp = subject_charts_view(request)

    signals, fields = wfdb.io.rdsamp(record_name=f'Subject{num}_AccTempEDA', pb_dir='noneeg')
    signals_SpO2HR, fields_SpO2HR = wfdb.io.rdsamp(record_name=f'Subject{num}_SpO2HR', pb_dir='noneeg')
    
    temp_array = signals[:,3]
    eda_array = signals[:,4]
    hr_array = signals_SpO2HR[:,1] # hr data is in another file.
    temps = temp_array.tolist()
    eda = eda_array.tolist()
    hr = hr_array.tolist()
    eda_data = json.dumps(eda, indent=4)
    data = json.dumps(temps, indent=4) #this runs fine. type(data) is str
    hr_data = json.dumps(hr, indent=4)

    context = {
        "Number": patient.subject_number,
        "Age": patient.age,
        "Gender": patient.gender,
        "Height": patient.height_cm,
        "Weight": patient.weight_kg,
        "temp_array": data,
        "eda_array": eda_data,
        "hr_array": hr_data,
    }

    
    return render(request, 'subjects/detail.html', context)

def subject_charts_view(request):
    print("is the data displayed?")

    num = request.GET.get('subject') #obtain the value of a GET variable with the name 'subject'
    patient = subject.objects.get(id=num)

    signals, fields = wfdb.io.rdsamp(record_name=f'Subject{num}_AccTempEDA', pb_dir='noneeg')
    
    temp_array = signals[:,3] 
    l = temp_array.tolist()
    data = json.dumps(l, indent=4) #this runs fine. type(data) is str

    context = {
        "temp_array": data
    }
    print(data)
    return render(request, 'subjects/temp_data.html', context)