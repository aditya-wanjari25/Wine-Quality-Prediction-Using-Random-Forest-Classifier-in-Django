from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import UserForm
import joblib
import numpy as np
from django.contrib import messages

# Create your views here.
def calculate(obj):
    # print(obj.Fixed_Acidity)
    Fixed_Acidity = float(obj.Fixed_Acidity)
    Volatile_Acidity = float(obj.Volatile_Acidity)
    Citric_Acid = float(obj.Citric_Acid)
    Residual_Sugar = float(obj.Residual_Sugar)
    Chlorides = float(obj.Chlorides)
    Free_SulphurDioxode = float(obj.Free_SulphurDioxode)
    Total_SulphurDioxide = float(obj.Total_SulphurDioxide)
    Density = float(obj.Density)
    pH = float(obj.pH)
    Sulphates = float(obj.Sulphates)
    Alchohol = float(obj.Alchohol)
    user_input = (Fixed_Acidity,Volatile_Acidity,Citric_Acid, Residual_Sugar, Chlorides, Free_SulphurDioxode,Total_SulphurDioxide,Density,pH,Sulphates,Alchohol)
    user_input = np.asarray(user_input)
    # print(user_input)
    model = joblib.load("WineQualityPredict.joblib")
    input_data_reshaped = user_input.reshape(1,-1)

    prediction = model.predict(input_data_reshaped)
    # print(prediction)

    if (prediction[0]==1):
      return "Good Quality Wine"
    else:
      return "Bad Quality Wine"





def index(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            obj = form.save()
            # print("Yes")
            answer = calculate(obj)
            messages.success(request, answer)

               
    context = {'form':form}
    return render(request, "index.html", context)


# input_data = (7.3,.65,0,1.2,0.065,15,21,0.9946,3.39,0.47,10)
# model = joblib.load("WineQualityPredict.joblib")
# # changing the input data to a numpy array
# input_data_as_numpy_array = np.asarray(input_data)

# # reshape the data as we are predicting the label for only one instance
# input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

# prediction = model.predict(input_data_reshaped)
# # print(prediction)

# if (prediction[0]==1):
#   print('Good Quality Wine')
# else:
#   print('Bad Quality Wine')