from django.shortcuts import render

# Create your views here.
def index (request):
    context = {"mensaje":"Ofrecemos servicios de reparacion de computadoras, mantenimiento y soporte tecnico."}
    return render(request, "myapp/index.html", context)