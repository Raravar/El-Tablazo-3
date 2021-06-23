from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/index.html')
def contacto(request):
    return render(request, 'core/contacto.html')  
def about(request):
    return render(request, 'core/about.html')  
def dulce(request):
    return render(request, 'core/dulce.html')
def salada(request):
    return render(request, 'core/salada.html')  
def mixta(request):
    return render(request, 'core/mixta.html')  
def registro(request):
    return render(request, 'core/registro.html')
