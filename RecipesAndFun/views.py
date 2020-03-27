from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as do_login
from .models import ingrediente,receta
from .forms import RecetaForm
from django.utils import timezone

# Create your views here.
def bienvenida(request):

    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request, "welcome.html")
    # En otro caso redireccionamos al login
    return redirect('/login')

def register(request):
    # Creamos el formulario de autenticación vacío
    form = UserCreationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UserCreationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            user = form.save()

            # Si el usuario se crea correctamente
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "register.html", {'form': form})

def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "login.html", {'form': form})

def create_recipe(request,):
    if request.method == "POST":
        form = RecetaForm(request.POST)
        if form.is_valid():
            receta = form.save(commit=False)
            #receta.autor = request.user
            receta.fecha_publicacion = timezone.now()
            receta.save()
            return redirect('/createrecipe', pk=receta.pk)
    else:
        form = RecetaForm()
    return render(request, 'createrecipe.html', {'form': form})

def myrecipes(request): #id
    #ownrecipes=receta.objects.filter(autor=id)
    ownrecipes= receta.objects.all()
    context={
        "ownrecipes":ownrecipes,
        #"id": id
    }
    return render(request, 'myrecipes.html', context)

def logout(request):
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')

# Mostrar ingredientes por tipo:
"""def ingredient_list(request):
    data = {}
    data['carne'] = ingrediente.objects.filter(tipo='carne')
    data['pescado'] = ingrediente.objects.filter(tipo='pescado')
    data['vegetal'] = ingrediente.objects.filter(tipo='vegetal')
    data['pasta'] = ingrediente.objects.filter(tipo='pasta')
    data['arroz'] = ingrediente.objects.filter(tipo='arroz')
    #data['cereal'] = ingrediente.objects.filter(tipo='cereal')
    data['lacteo'] = ingrediente.objects.filter(tipo='lacteo')
    data['fruta'] = ingrediente.objects.filter(tipo='fruta')
    #data['especia'] = ingrediente.objects.filter(tipo='especia')
    #data['otros'] = ingrediente.objects.filter(tipo='otros')
    data['huevos'] = ingrediente.objects.filter(tipo='huevos')
    data['legumbres'] = ingrediente.objects.filter(tipo='legumbres')
    data['frutossecos'] = ingrediente.objects.filter(tipo='frutossecos')
    #data['aceite'] = ingrediente.objects.filter(tipo='aceite')
    #data['harina'] = ingrediente.objects.filter(tipo='harina')
    #data['azucar'] = ingrediente.objects.filter(tipo='azucar')
    #data['vinagre'] = ingrediente.objects.filter(tipo='vinagre')

    return render(request, "listaIngredientes.html", {'data': data})"""

def recipe_list(request):
    datos = {}
    datos['pollo'] = receta.objects.filter(ingredientes__contains='pollo')
    datos['salmon'] = receta.objects.filter(ingredientes__contains='salmon')
    datos['tomate'] = receta.objects.filter(ingredientes__contains='tomate')
    datos['espaguetis'] = receta.objects.filter(ingredientes__contains='espaguetis')
    datos['arroz'] = receta.objects.filter(ingredientes__contains='arroz')
    datos['queso'] = receta.objects.filter(ingredientes__contains='queso')
    datos['huevos'] = receta.objects.filter(ingredientes__contains='huevos')
    datos['lentejas'] = receta.objects.filter(ingredientes__contains='lentejas')
    datos['nueces'] = receta.objects.filter(ingredientes__contains='nueces')
    datos['fresa'] = receta.objects.filter(ingredientes__contains='fresa')

    return render(request, "listaIngredientes.html", {'datos':datos})

def see_recipe(request):
    receti={}
    receti=receta.objects.all()
    return render(request, "verReceta.html",{'receti':receti})