from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as do_login
from .models import ingrediente,receta
from .forms import RecetaForm
from django.utils import timezone
from django.views.generic import DetailView

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
            receta.autor = request.user
            receta.fecha_publicacion = timezone.now()
            receta.save()
            return redirect('/createrecipe', pk=receta.pk)
    else:
        form = RecetaForm()
    return render(request, 'createrecipe.html', {'form': form})

def logout(request):
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')

def ingredient_list(request):
    context={}
    #TIPOS DE COMIDA EN NUESTRA APLICACION
    tipo_comida ={}
    tipo_comida['carne'] = ingrediente.objects.filter(tipo='carne')
    tipo_comida['pescado'] = ingrediente.objects.filter(tipo='pescado')
    tipo_comida['vegetal'] = ingrediente.objects.filter(tipo='vegetal')
    tipo_comida['pasta'] = ingrediente.objects.filter(tipo='pasta')
    tipo_comida['arroz'] = ingrediente.objects.filter(tipo='arroz')
    #tipo_comida['cereal'] = ingrediente.objects.filter(tipo='cereal')
    tipo_comida['lacteo'] = ingrediente.objects.filter(tipo='lacteo')
    tipo_comida['fruta'] = ingrediente.objects.filter(tipo='fruta')
    #tipo_comida['especia'] = ingrediente.objects.filter(tipo='especia')
    #tipo_comida['otros'] = ingrediente.objects.filter(tipo='otros')
    tipo_comida['huevos'] = ingrediente.objects.filter(tipo='huevos')
    tipo_comida['legumbres'] = ingrediente.objects.filter(tipo='legumbres')
    tipo_comida['frutossecos'] = ingrediente.objects.filter(tipo='frutossecos')
    #tipo_comida['aceite'] = ingrediente.objects.filter(tipo='aceite')
    #tipo_comida['harina'] = ingrediente.objects.filter(tipo='harina')
    #tipo_comida['azucar'] = ingrediente.objects.filter(tipo='azucar')
    #tipo_comida['vinagre'] = ingrediente.objects.filter(tipo='vinagre')

    #INGREDIENTES DE NUESTRAS RECETAS
    recetas_de = {}
    recetas_de['pollo'] = receta.objects.filter(ingredientes__contains='pollo')
    recetas_de['salmon'] = receta.objects.filter(ingredientes__contains='salmon')
    recetas_de['tomate'] = receta.objects.filter(ingredientes__contains='tomate')
    recetas_de['espaguetis'] = receta.objects.filter(ingredientes__contains='espaguetis')
    recetas_de['arroz'] = receta.objects.filter(ingredientes__contains='arroz')
    recetas_de['queso'] = receta.objects.filter(ingredientes__contains='queso')
    recetas_de['huevos'] = receta.objects.filter(ingredientes__contains='huevos')
    recetas_de['lentejas'] = receta.objects.filter(ingredientes__contains='lentejas')
    recetas_de['nueces'] = receta.objects.filter(ingredientes__contains='nueces')
    recetas_de['fresas'] = receta.objects.filter(ingredientes__contains='fresas')

    context={
        'recetas_de':recetas_de,
        'tipo_comida':tipo_comida
    }
    return render(request, "listaIngredientes.html", context)

def myrecipes(request):
    ownrecipes=receta.objects.filter(autor=request.user.id)
    return render(request, 'myrecipes.html', {"ownrecipes":ownrecipes})

class RecipeDetail(DetailView):
    model = receta
    template_name = 'verReceta.html'

    def get_context_data(self, **kwargs):
        context = super(RecipeDetail, self).get_context_data(**kwargs)
        return context
