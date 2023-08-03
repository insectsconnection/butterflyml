
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login,logout,authenticate #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
from django.views.generic import TemplateView  # Import TemplateView
import os
import pickle

from django.utils.deconstruct import deconstructible
@deconstructible


# create your views here and add parameters title
def index(request):
    
    # Get all Posts
    return render(request, 'lepidoptera/index.html')


def classify(request):
    # Get all Posts
    return render(request, 'lepidoptera/classify.html')


def base(request):
    # Get all Posts
    return render(request, 'lepidoptera/base.html')


def data(request):
    def get(self, request, **kwargs):
        # we will pass this context object into the
        # template so that we can access the data
        # list in the template
        context = {
            'data': [
                {
                    'name': 'Celeb 1',
                    'worth': '3567892'
                },
                {
                    'name': 'Celeb 2',
                    'worth': '23000000'
                },
                {
                    'name': 'Celeb 3',
                    'worth': '1000007'
                },
                {
                    'name': 'Celeb 4',
                    'worth': '456789'
                },
                {
                    'name': 'Celeb 5',
                    'worth': '7890000'
                },
                {
                    'name': 'Celeb 6',
                    'worth': '12000456'
                },
                {
                    'name': 'Celeb 7',
                    'worth': '896000'
                },
                {
                    'name': 'Celeb 8',
                    'worth': '670000'
                }
            ]
        }

        return render(request, 'lepidoptera/data.html', context)


def dashboard(request):
    # Get all Posts
    return render(request, 'lepidoptera/dashboard.html')


def butterfly(request):
    # Get all Posts
    return render(request, 'lepidoptera/butterfly.html')


def covnet(request):
    # Get all Posts
    return render(request, 'lepidoptera/covnet.html')


def navbar(request):
    # Get all Posts
    return render(request, 'lepidoptera/nav-bar.html')


def weather(request):
    # Get all Posts
    return render(request, 'lepidoptera/weather.html')

def main(request):
    # Get all Posts
    return render(request, 'lepidoptera/main.html')


# custom method for generating predictions
def getPredictions(pclass, sex, age, sibsp, parch, fare, C, Q, S):
   
    model = pickle.load(open("data/titanic_train.csv", "rb"))
    scaled = pickle.load(open("scaler.sav", "rb"))
    prediction = model.predict(sc.transform([[pclass, sex, age, sibsp, parch, fare, C, Q, S]]))
    
    if prediction == 0:
        return "not survived"
    elif prediction == 1:
        return "survived"
    else:
        return "error"
        

# our result page view
def result(request):
    pclass = int(request.GET['pclass']) 
    sex = int(request.GET['sex'])
    age = int(request.GET['age'])
    sibsp = int(request.GET['sibsp'])
    parch = int(request.GET['parch'])
    fare = int(request.GET['fare'])
    embC = int(request.GET['embC'])
    embQ = int(request.GET['embQ'])
    embS = int(request.GET['embS'])

    result = getPredictions(pclass, sex, age, sibsp, parch, fare, embC, embQ, embS)

    return render(request, 'lepidoptera/result.html', {'result':result})

def restnet(request):
    # Get all Posts
    return render(request, 'lepidoptera/restnet.html')


def objectmeasurement(request):
    # Get all Posts
    return render(request, 'lepidoptera/object_measurement.html')

def objectidentifier(request):
    # Get all Posts
    return render(request, 'lepidoptera/object_identifier.html')

# def gen(camera):
#     while True:
#         frame = camera.get_frame() 
#         yield(b'--frame\r\n'b'Content-Type:image/jpeg\r\n\r\n' + frame + b\r\n\r\n')
    
# def video_feed(request):
#     return StreamingHttpResponse(gen(VideoCamera()), content_type+'multiple/x-mixed-replace; boundary=frame')


def adddevice(request):
    # Get all Posts
    return render(request, 'lepidoptera/adddevice.html')


def butterfly(request):
    # Get all Posts
    return render(request, 'lepidoptera/butterfly.html')


def camera(request):
    # Get all Posts
    return render(request, 'lepidoptera/camera.html')

def registration_request(request):
    # Get all Posts
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("main:homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="lepidoptera/main/login.html", context={"login":form})


def login_request(request):
    return render(request, 'lepidoptera/main/login.html')


def logout_reques(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect(request, 'lepidoptera/main/home.html')