from django.shortcuts import render

def cocina(request):
    return render(request, 'cocina.html', {})