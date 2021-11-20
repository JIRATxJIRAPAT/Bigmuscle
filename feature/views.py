
# Create your views here.
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from Users.models import Customer


def bdTest(request):
    if request.method == "POST":

        weight = float(request.POST["weight"])
        height = float(request.POST["height"])/100
        heightcm = float(request.POST["height"])
        
        x = request.user.customer.id
        val = Customer.objects.filter(id=x)
        val.update(weight=weight)
        val.update(height=heightcm)

        bmi = "{:.2f}".format(weight / (height ** 2))
        floatBmi = float(bmi)
        val.update(bmi=floatBmi)
        if floatBmi < 18.5:
            result = "Underweight"

        elif floatBmi >= 18.5 and floatBmi < 24.9:
            result = "Normal weight"

        elif floatBmi >= 25 and floatBmi < 29.9:
            result = "Overweight"

        else:
            result = "Obese"

        return render(request, "feature/bdTestresult.html", {
            "bmi": bmi,
            "result": result,
            "weight": weight,
            "height": height,
            "val": val,
            "x": x,
        })
    return render(request, 'feature/bdTest.html')

