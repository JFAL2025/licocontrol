from django.shortcuts import render

# Create your views here.
def panel(request):
    return render(request, 'panel.html')

def registro_v(request):
    return render(request, 'registro_v.html')

def inventario(request):
    return render(request, 'inventario.html')
def reporte(request):
    return render(request, 'reporte.html')
def catalogo(request):
    return render(request, 'catalogo.html')