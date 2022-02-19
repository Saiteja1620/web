from django.shortcuts import render

def index(request):
	return render(request, 'index.html')

def questions(request):
	return render(request, 'quiz.html')

def questionsV(request):
	return render(request, 'quizV.html')

def questionsA(request):
	return render(request, 'quizA.html')

def login(request):
	return render(request, 'username.html')

def register(request):
	return render(request,'registration.html')