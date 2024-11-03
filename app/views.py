from django.shortcuts import render

# Create your views here.
def questions_listing(request):
    return render(request, "index.html")

#def question(request, question_id):
#   return render(request, "question.html", {"question": question_id})
def question(request):
   return render(request, "question.html")

def new_question(request):
    return render(request, "ask.html")

def login(request):
    return render(request, "login.html")

def signup(request):
    return render(request, "signup.html")

def settings(request):
    return render(request, "settings.html")