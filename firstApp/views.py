from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from firstApp.models import Medico
from firstApp.models import Pacientes
from firstApp.models import Cita
from firstApp.forms import FormMedico
from firstApp.forms import FormPaciente
from firstApp.forms import FormCita


# Create your views here.+


def index(request):
    return render(request, 'firstApp/index.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(email, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
    return render(request, 'firstApp/log_register.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    return render(request, 'firstApp/log_inicioSesion.html')

def logout_view(request):
    logout(request)
    return redirect('/')






@login_required
def medicos(request):
    medicos = Medico.objects.all()
    data = {'medicos' : medicos}
    return render(request, 'firstApp/medicos.html', data)
@login_required
def pacientes(request):
    pacientes = Pacientes.objects.all()
    data = {'pacientes' : pacientes}
    return render(request, 'firstApp/pacientes.html', data)
@login_required
def citas(request):
    citas = Cita.objects.all()
    data = {'citas' : citas}
    return render(request, 'firstApp/citas.html', data)



@login_required
def agregarMedico(request):
    form = FormMedico()
    if request.method == 'POST' :
        form = FormMedico(request.POST)
        if form.is_valid() :
            form.save()
        return redirect("medicos")
    data = {'form' : form}
    return render(request, 'firstApp/agregarMedicos.html', data)
@login_required
def eliminarMedico(request, id):
    medico = Medico.objects.get(id = id)
    medico.delete()
    medicos = Medico.objects.all()
    data ={'medicos': medicos}
    return render(request,'firstApp/medicos.html',data)
@login_required
def actualizarMedico(request, id):
    medico = Medico.objects.get(id = id)
    form = FormMedico(instance=medico)
    if request.method == 'POST' :
        form = FormMedico(request.POST, instance=medico)
        if form.is_valid() :
            form.save()
        return redirect("medicos")
    data = {'form' : form}
    return render(request, 'firstApp/agregarMedicos.html', data)




@login_required
def agregarPaciente(request):
    form = FormPaciente()
    if request.method == 'POST' :
        form = FormPaciente(request.POST)
        if form.is_valid() :
            form.save()
        return redirect("pacientes")
    data = {'form' : form}
    return render(request, 'firstApp/agregarPacientes.html', data)
@login_required
def eliminarPaciente(request, id):
    paciente = Pacientes.objects.get(id = id)
    paciente.delete()
    pacientes = Pacientes.objects.all()
    data ={'pacientes': pacientes}
    return render(request,'firstApp/pacientes.html',data)
@login_required
def actualizarPaciente(request, id):
    paciente = Pacientes.objects.get(id = id)
    form = FormPaciente(instance=paciente)
    if request.method == 'POST' :
        form = FormPaciente(request.POST, instance=paciente)
        if form.is_valid() :
            form.save()
        return redirect("pacientes")
    data = {'form' : form}
    return render(request, 'firstApp/agregarPacientes.html', data)




@login_required
def agregarCitas(request):
    form = FormCita()
    if request.method == 'POST' :
        form = FormCita(request.POST)
        if form.is_valid() :
            form.save()
        return redirect("citas")
    data = {'form' : form}
    return render(request, 'firstApp/agregarCita.html', data)
@login_required
def eliminarCitas(request, id):
    cita = Cita.objects.get(id = id)
    cita.delete()
    citas = Pacientes.objects.all()
    data ={'citas': citas}
    return render(request,'firstApp/citas.html',data)
@login_required
def actualizarCitas(request, id):
    cita = Cita.objects.get(id = id)
    form = FormCita(instance=cita)
    if request.method == 'POST' :
        form = FormCita(request.POST, instance=cita)
        if form.is_valid() :
            form.save()
        return redirect("citas")
    data = {'form' : form}
    return render(request, 'firstApp/agregarCita.html', data)