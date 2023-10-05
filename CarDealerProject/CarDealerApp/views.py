from django.shortcuts import render
from CarDealerApp.models import Flota, Chofer, PuntoDeRetiro
from CarDealerApp.forms import FormCargarFlota, FormCargarChofer, FormPuntoDeRetiro, FormBuscarFlota

# Renders de querys
def flota(request):
    flota = Flota.objects.all()
    contexto = {"flota": flota} 
    return render(request, "CarDealerApp/listadoFlota.html", contexto)

def choferes(request):
    choferes = Chofer.objects.all()
    contexto = {"choferes": choferes} 
    return render(request, "CarDealerApp/listadoChoferes.html", contexto)

def puntosDeRetiro(request):
    puntosDeRetiro = PuntoDeRetiro.objects.all()
    contexto = {"puntosDeRetiro": puntosDeRetiro} 
    return render(request, "CarDealerApp/listadoPuntosDeRetiro.html", contexto)


# Cargar nuevo vehículo en Flota
def cargarFlota(request):
    if request.method == 'POST':
        nuevoVehiculo = FormCargarFlota(request.POST)

        if nuevoVehiculo.is_valid():
            dato = nuevoVehiculo.cleaned_data
            flota = Flota(
                marcaModelo=dato['marcaModelo'],
                anio=dato['anio'],
                km=dato['km'],
                transmision=dato['transmision'],
                combustible=dato['combustible'],
                costo=dato['costo'],
                foto=dato['foto'])
            flota.save()
            return render(request, 'CarDealerApp/cargaFlotaExito.html')
        else:
            print(f"\n\n contenido inválido: {nuevoVehiculo.errors} \n\n")
    else:
        nuevoVehiculo = FormCargarFlota()

    return render(request, 'CarDealerApp/cargarFlota.html',{"nuevoVehiculo": nuevoVehiculo})


# Cargar nuevo Chofer
def cargarChofer(request):
    if request.method == 'POST':
        nuevoChofer = FormCargarChofer(request.POST)

        if nuevoChofer.is_valid():
            dato = nuevoChofer.cleaned_data
            chofer = Chofer(
                nombre=dato['nombre'],
                apellido=dato['apellido'],
                puesto=dato['puesto'],
                foto=dato['foto'])
            chofer.save()
            return render(request, 'CarDealerApp/cargaChoferExito.html')
        else:
            print(f"\n\n contenido inválido: {nuevoChofer.errors} \n\n")
    else:
        nuevoChofer = FormCargarChofer()

    return render(request, 'CarDealerApp/cargarChofer.html',{"nuevoChofer": nuevoChofer})


# Cargar nuevo Punto de Retiro
def cargarPuntoDeRetiro(request):
    if request.method == 'POST':
        nuevoPuntoDeRetiro = FormPuntoDeRetiro(request.POST)

        if nuevoPuntoDeRetiro.is_valid():
            dato = nuevoPuntoDeRetiro.cleaned_data
            puntoDeRetiro = PuntoDeRetiro(
                provincia=dato['provincia'],
                localidad=dato['localidad'],
                direccion=dato['direccion'],
                telefono=dato['telefono'],
                email=dato['email'])
            puntoDeRetiro.save()
            return render(request, 'CarDealerApp/cargaPuntoDeRetiroExito.html')
        else:
            print(f"\n\n contenido inválido: {nuevoPuntoDeRetiro.errors} \n\n")
    else:
        nuevoPuntoDeRetiro = FormPuntoDeRetiro()

    return render(request, 'CarDealerApp/cargarPuntoDeRetiro.html',{"nuevoPuntoDeRetiro": nuevoPuntoDeRetiro})


# Buscador en la home
def buscarFlota(request):
    if request.method == 'POST':
        formBuscar = FormBuscarFlota(request.POST)

        if formBuscar.is_valid():
            dato = formBuscar.cleaned_data
            flota = Flota.objects.filter(marcaModelo__icontains=dato["marcaModelo"])
            return render(request, 'CarDealerApp/resultadosBusqueda.html', {"flota": flota})
        else:
            print(f"\n\n contenido INVALIDO: {formBuscar.errors} \n\n")
    else:
        formBuscar = FormBuscarFlota()

    return render(request, 'CarDealerApp/home.html',{"formBuscar": formBuscar})
