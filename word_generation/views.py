from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CreateUserForm
from .models import testResults
from django.core.files import File
from django.contrib.auth import authenticate, login as login_auth, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Max, Min
import random
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, "word_generation/index.html")

def register(request):

    if request.user.is_authenticated:
        return redirect('typing_test:test')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "Account created with username: " + user)
                return redirect('typing_test:login')
        
        context = {'form': form}
        return render(request, "word_generation/register.html", context)

def login(request):
    if request.user.is_authenticated:
        return redirect('typing_test:test')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password)

            if user is not None:
                login_auth(request, user)
                return redirect('typing_test:test')
            else:
                messages.info(request, "Invalid data entered.")

        return render(request, "word_generation/login.html")

def userLogout(request):
    logout(request)
    return redirect('typing_test:login')

@login_required(login_url = 'typing_test: login')
def test(request):
    words = [[], [], [], [], [], []]
    f = open("../TYPING_WEBSITE/wordlist_filter.txt", "r")
    for word in f.read().split("\n"):
        word = word.strip()
        words[len(word) - 3].append(word)

    """
    Number of words of each kind (no of characters):
    3 characters - 10 
    4 characters - 10 
    5 characters - 11 
    6 characters - 7 
    7 characters - 7 
    8 characters - 5 
    """
    word_limits = [10, 10, 11, 7, 7, 5]
    word_counts = [0, 0, 0, 0, 0, 0]
    text = ""

    index_choice = [0, 1, 2, 3, 4, 5]

    while True:
        if len(index_choice) == 0:
            break
        choice = random.choice(index_choice)
        word_counts[choice] += 1
        if word_counts[choice] == word_limits[choice]:
            index_choice.remove(choice)
        text += random.choice(words[choice]) + " "    
    
    return render(request, "word_generation/typing-test.html", {
        "test_text": text
    })

@login_required(login_url = 'typing_test: login')
def result(request):
    if request.method == "POST":
        WPM = request.POST.get('WPMsub')
        if WPM == 'NaN':
            WPM = 0
        accuracy = request.POST.get('accuracysub')
        timeTaken = request.POST.get('timesub')
        t1 = testResults.objects.create(owner = request.user, WPM = WPM, accuracy = accuracy, timeTaken = timeTaken, testDone = datetime.now())
        return redirect('typing_test:test')
    return render(request, "word_generation/results.html")

@login_required(login_url = 'typing_test: login')
def user(request):
    #need to access all the user tests and pass it to template
    #need to link all urls
    tests = testResults.objects.all().filter(owner = request.user)
    maxWPM = testResults.objects.all().filter(owner = request.user).aggregate(Max('WPM'))['WPM__max']
    maxAccuracy = testResults.objects.all().filter(owner = request.user).aggregate(Max('accuracy'))['accuracy__max']
    minTime = testResults.objects.all().filter(owner = request.user).aggregate(Min('timeTaken'))['timeTaken__min']
    last5tests = testResults.objects.filter(owner = request.user).order_by('testDone')[:5]
    b = []
    for i in range(len(last5tests)):
        str1 = "Test #" + str(i+1)
        b.append([str1, last5tests[i].WPM])
    for i in range(len(b),5):
        str1 = "Test #" + str(i+1)
        b.append([str1, 0])
    context = {"data": b, "maxWPM": maxWPM, "maxAccuracy": maxAccuracy, "minTime":minTime}
    return render(request, "word_generation/user.html", context)

def info(request):
    return render(request, "word_generation/how-to.html")