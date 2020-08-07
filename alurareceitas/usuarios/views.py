from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from receitas.models import Receita



def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        if not nome.strip():
            print('O campo nome  não pode ficar em branco') 
            return redirect('cadastro')
        if not email.strip():
            print('O campo email  não pode ficar em branco') 
            return redirect('cadastro') 
        if senha != senha2:
            print('Senha não são iguais')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            print('Usuário já cadastrado!')
            return redirect('cadastro')
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        print('Usuário cadastrado com sucesso!')      
        return redirect('login')  
    else:    
        return render(request, 'usuarios/cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == '' or senha == '':
            print('Os campos email e senha não podem ficar em branco')
            return redirect('login')
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)            
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
    else:    
        return render(request, 'usuarios/login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'usuarios/dashboard.html')
    else:
        return redirect('login')

def cria_receita(request):
    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_receita = request.FILES['foto_receita']
        return redirect('dashboard')
    else:
        return render(request, 'usuarios/cria_receita.html')
 