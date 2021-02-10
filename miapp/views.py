from django.shortcuts import render, HttpResponse, redirect

from miapp.models import Curso
from miapp.models import Carrera
from django.db.models import Q

from miapp.forms import FormCurso
from miapp.forms import FormCarrera
from django.contrib import messages

# Create your views here.
layout = """
    <h1> Exámen Final (LP3) || </h1>
    <hr/>
    <ul>
        <li>
            <a href="/inicio">Inicio</a>
        </li>
    </ul>
    <hr/>
"""

def index(request):
    estudiantes = [
        'Colan Aranibar Brian Lee',
        'Quispe Calixto Javie',
        'Vite Cochachin Sergio',
        'Ramirez Huamani Paulo'
    ]
    
    return render(request, 'index.html', {
        'titulo': 'Inicio',
        'mensaje': 'Exámen Final',
        'estudiantes': estudiantes
    })








def listar_cursos(request):
    cursos = Curso.objects.all()
    """
    cursos = Curso.objects.filter(
        Q(titulo__contains="Py") |
        Q(titulo__contains="Hab")
    )
    """
    return render(request, 'listar_cursos.html',{
        'cursos': cursos,
        'titulo': 'Listado de Cursos'
    })

def crear_curso(request, titulo, contenido, publicado):
    curso = Curso(
        titulo = titulo,
        contenido = contenido,
        publicado = publicado
    )
    curso.save()
    return HttpResponse(f"Curso Creado: {curso.titulo} - {curso.contenido}")

def create_curso(request):
    if request.method == 'POST':
        formulario = FormCurso(request.POST)
        if formulario.is_valid():
            data_form = formulario.cleaned_data
            titulo = data_form.get('titulo')
            contenido = data_form['contenido']
            publicado = data_form['publicado']
            curso = Curso(
                titulo = titulo,
                contenido = contenido,
                publicado = publicado
            )
            curso.save()

            #Es para crear un mensaje Flash (Solo se muestra una vez)
            messages.success(request,f'Se agregó correctamente el curso {curso.id}')

            return redirect('listar_cursos')
            #return HttpResponse(curso.titulo + ' - ' + curso.contenido + ' - ' + str(curso.publicado))
    else:
        formulario = FormCurso()        
    return render(request, 'create_curso.html',{
        'form': formulario
    })

def buscar_curso(request):
    try:
        curso = Curso.objects.get(id=2)
        resultado = f"""Curso: 
                        <br> <strong>ID:</strong> {curso.id} 
                        <br> <strong>Título:</strong> {curso.titulo} 
                        <br> <strong>Contenido:</strong> {curso.contenido}
                        """
    except:
        resultado = "<h1> Curso No Encontrado </h1>"
    return HttpResponse(resultado)

def editar_curso(request, id):
    curso = Curso.objects.get(pk=id)

    curso.titulo = "Enseñanza onLine en la UNTELS"
    curso.contenido = "Aula Virtual, Google Meet, Portal Académico, Google Classroom..."
    curso.publicado = False

    curso.save()
    return HttpResponse(f"Curso Editado: {curso.titulo} - {curso.contenido}")

def eliminar_curso(request, id):
    curso = Curso.objects.get(pk=id)
    curso.delete()
    return redirect('listar_cursos')

def save_curso(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        if len(titulo)<=5:
            return HttpResponse("<h2>El tamaño del título es pequeño, intente nuevamente</h2>")
        contenido = request.POST['contenido']
        publicado = request.POST['publicado']

        curso = Curso(
            titulo = titulo,
            contenido = contenido,
            publicado = publicado
        )
        curso.save()
        return HttpResponse(f"Curso Creado: {curso.titulo} - {curso.contenido}")
    else:
        return HttpResponse("<h2> No se ha podido registrar el curso </h2>")




def listar_carreras(request):
    carreras = Carrera.objects.all()
    """
    carreras = Carrera.objects.filter(
        Q(titulo__contains="Py") |
        Q(titulo__contains="Hab")
    )
    """
    return render(request, 'listar_carreras.html',{
        'carreras': carreras,
        'titulo': 'Listado de Carreras'
    })

def crear_carrera(request, titulo, contenido, publicado):
    carrera = Carrera(
        titulo = titulo,
        contenido = contenido,
        publicado = publicado
    )
    carrera.save()
    return HttpResponse(f"Carrera Creado: {carrera.titulo} - {carrera.contenido}")

def create_carrera(request):
    if request.method == 'POST':
        formulario = FormCarrera(request.POST)
        if formulario.is_valid():
            data_form = formulario.cleaned_data
            titulo = data_form.get('titulo')
            contenido = data_form['contenido']
            publicado = data_form['publicado']
            carrera = Carrera(
                titulo = titulo,
                contenido = contenido,
                publicado = publicado
            )
            carrera.save()

            #Es para crear un mensaje Flash (Solo se muestra una vez)
            messages.success(request,f'Se agregó correctamente el carrera {carrera.id}')

            return redirect('listar_carreras')
            #return HttpResponse(carrera.titulo + ' - ' + carrera.contenido + ' - ' + str(carrera.publicado))
    else:
        formulario = FormCarrera()        
    return render(request, 'create_carrera.html',{
        'form': formulario
    })

def buscar_carrera(request):
    try:
        carrera = Carrera.objects.get(id=2)
        resultado = f"""Carrera: 
                        <br> <strong>ID:</strong> {carrera.id} 
                        <br> <strong>Título:</strong> {carrera.titulo} 
                        <br> <strong>Contenido:</strong> {carrera.contenido}
                        """
    except:
        resultado = "<h1> Carrera No Encontrado </h1>"
    return HttpResponse(resultado)

def editar_carrera(request, id):
    carrera = Carrera.objects.get(pk=id)

    carrera.titulo = "Enseñanza onLine en la UNTELS"
    carrera.contenido = "Aula Virtual, Google Meet, Portal Académico, Google Classroom..."
    carrera.publicado = False

    carrera.save()
    return HttpResponse(f"Carrera Editado: {carrera.titulo} - {carrera.contenido}")

def eliminar_carrera(request, id):
    carrera = Carrera.objects.get(pk=id)
    carrera.delete()
    return redirect('listar_carreras')

def save_carrera(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        if len(titulo)<=5:
            return HttpResponse("<h2>El tamaño del título es pequeño, intente nuevamente</h2>")
        contenido = request.POST['contenido']
        publicado = request.POST['publicado']

        carrera = Carrera(
            titulo = titulo,
            contenido = contenido,
            publicado = publicado
        )
        carrera.save()
        return HttpResponse(f"Carrera Creado: {carrera.titulo} - {carrera.contenido}")
    else:
        return HttpResponse("<h2> No se ha podido registrar el carrera </h2>")



