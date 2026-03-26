from django.shortcuts import render

def letter(request):
		return render(request, "letter.html")