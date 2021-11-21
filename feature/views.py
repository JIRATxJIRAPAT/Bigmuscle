from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from Users.models import Customer


def bdTest(request):    
    
    if request.method == "POST":
        val = "None"
        isCus = False
        weight = float(request.POST["weight"])
        height = float(request.POST["height"])/100
        heightcm = float(request.POST["height"])
        bmi = "{:.2f}".format(weight / (height ** 2))
        floatBmi = float(bmi)

        if  request.user.is_authenticated:
            try:
                checkCus = Customer.objects.get(user=request.user)
            except Customer.DoesNotExist:
                checkCus = None

            if checkCus is not None:
                x = request.user.customer.id
                val = Customer.objects.filter(id=x)
                val.update(weight=weight)
                val.update(height=heightcm)
                val.update(bmi=floatBmi)
                isCus = True
        
        
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
            "isCustomer": isCus
            #"val": val,
            #"x": x,
        })
    return render(request, 'feature/bdTest.html')

