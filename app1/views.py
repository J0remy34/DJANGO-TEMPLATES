from django.shortcuts import render

# Create your views here.
def v1(request):
    data = {"nombre":"jeremy","Apellido":"Rincon","edad":24}
    return render(request, 'app1/app1v1.html',data)

def v2(request):
    data = {"nombre":"Luis","Apellido":"Arriagada","edad":40, "foto":"personal.jpg"}
    return render(request, 'app1/app1v2.html', data)