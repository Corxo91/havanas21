from django.shortcuts import render, redirect

def bar(request):
    return render(request, 'cafe.html')

def salon(request):
    return render(request, 'salon.html')
