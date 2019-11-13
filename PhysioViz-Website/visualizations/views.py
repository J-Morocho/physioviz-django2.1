from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def subject_chart(request):
    num = 1
    return render(request, 'visualizations/index.html', {})