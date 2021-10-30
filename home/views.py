from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request,"home/index.html",{
    })

def bdTest(request):
    if request.method == "POST":
        weight = float(request.POST["weight"])
        height = float(request.POST["height"])/100

        
        bmi = "{:.2f}".format(weight / (height ** 2))
        floatBmi = float(bmi)
        if floatBmi < 18.5:
            result = "Underweight"
        elif floatBmi >= 18.5 and floatBmi < 24.9:
            result = "Normal weight"
        elif floatBmi >= 25 and floatBmi < 29.9:
            result = "Overweight"
        else:
            result = "Obese"
        
        
            
        return render(request, "home/bdTest.html", {
            "bmi": bmi,
            "result": result
        })    
    return render(request, 'home/bdTest.html')