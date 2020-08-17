from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from receitas.models import Receita



def cadastro(request):
    """Cadastra um novo usuário no sistema"""
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        if campo_vazio(nome):
            messages.error(request,'O campo nome  não pode ficar em branco') 
            return redirect('cadastro')
        if campo_vazio(email):
            messages.error(request,'O campo email  não pode ficar em branco') 
            return redirect('cadastro') 
        if senha != senha2:
            messages.error(request, 'As senhas não são iguais')            
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            messages.success(request,'Usuário já cadastrado!')
            return redirect('cadastro')
        if User.objects.filter(username=nome).exists():
            print('Usuário já cadastrado!')
            return redirect('cadastro')
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()        
        messages.success(request, 'Cadastro realizado com sucesso!')      
        return redirect('login')  
    else:    
        return render(request, 'usuarios/cadastro.html')

def login(request):
    """Realiza login do usuário no sistema"""
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
    """Realiza logout de um usuário no sistema"""
    auth.logout(request)
    return redirect('login')

def dashboard(request):
    """Apresenta as receitas criadas do usuário logado"""
    if request.user.is_authenticated:
        id = request.user.id
        receitas = Receita.objects.order_by('-data_receita').filter(pessoa=id)
        dados = {
            'receitas' : receitas
        }
        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('login')
 
def campo_vazio(campo):
    """Verifica campos vazios"""
    return not campo.strip()