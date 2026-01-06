from django.shortcuts import render
from .services import (
    convert_length,LENGTH_FACTORS,
    WEIGHT_FACTORS, convert_weight,
    convert_temperature
    )


def home(request):
    return render(request,"converter/home.html")


def length(request):
    units = list(LENGTH_FACTORS.keys())

    result = None
    error = None

    #defaults for first page load
    value = ""
    from_unit = "meter"
    to_unit = "kilometer"

    if request.method == "POST":
        value = request.POST.get("value", "").strip()
        from_unit = request.POST.get("from_unit", from_unit)
        to_unit = request.POST.get("to_unit", to_unit)

        if from_unit not in LENGTH_FACTORS or to_unit not in LENGTH_FACTORS:
            error = "Invalid unit selection"

        else:
            #Validate number
            try:
                numeric_value = float(value)
                #Convert: from -> meters -> to
                converted = convert_length(numeric_value,from_unit,to_unit)
                result = round(converted,6)

            except:
                error = "Please enter a valid number"

    context = {
        "units" : units,
        "result" : result,
        "error" : error,
        "value" : value,
        "from_unit": from_unit,
        "to_unit": to_unit,
    }


    return render(request,"converter/length.html",context)

def weight(request):
    units = list(WEIGHT_FACTORS.keys())

    result = None
    error = None

    #defaults for first page load
    value = ""
    from_unit = "gram"
    to_unit = "kilogram"

    if request.method == "POST":
        value = request.POST.get("value", "").strip()
        from_unit = request.POST.get("from_unit", from_unit)
        to_unit = request.POST.get("to_unit", to_unit)

        if from_unit not in WEIGHT_FACTORS or to_unit not in WEIGHT_FACTORS:
            error = "Invalid unit selection"

        else:
            #Validate number
            try:
                numeric_value = float(value)
                #Convert: from -> meters -> to
                converted = convert_weight(numeric_value,from_unit,to_unit)
                result = round(converted,6)

            except:
                error = "Please enter a valid number"

    context = {
        "units" : units,
        "result" : result,
        "error" : error,
        "value" : value,
        "from_unit": from_unit,
        "to_unit": to_unit,
    }

    return render(request,"converter/weight.html",context)



def temperature(request):
    units = ["celsius", "fahrenheit", "kelvin"]

    result = None
    error = None

    #defaults for first page load
    value = ""
    from_unit = "gram"
    to_unit = "kilogram"

    if request.method == "POST":
        value = request.POST.get("value", "").strip()
        from_unit = request.POST.get("from_unit", from_unit)
        to_unit = request.POST.get("to_unit", to_unit)

        if from_unit not in units or to_unit not in units:
            error = "Invalid unit selection"

        else:
            #Validate number
            try:
                numeric_value = float(value)
                #Convert: from -> meters -> to
                converted = convert_temperature(numeric_value,from_unit,to_unit)
                result = round(converted,6)

            except:
                error = "Please enter a valid number"

    context = {
        "units" : units,
        "result" : result,
        "error" : error,
        "value" : value,
        "from_unit": from_unit,
        "to_unit": to_unit,
    }

    return render(request,"converter/temperature.html",context)