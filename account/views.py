from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, LoginForm, CustomerForm
from django.contrib.auth import authenticate, login, logout
from .models import User, Cliente
# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('users:login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    context = {'form' : form, 'msg' : msg}
    return render(request,'register.html', context)

def register_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:view_customers')  # Redirige a la lista de clientes después de agregar uno nuevo
    else:
        form = CustomerForm()

    context = {'form' : form}

    return render(request, 'register_customer.html', context)


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('map:home')
            elif user is not None and user.is_employee:
                login(request, user)
                return redirect('map:home_employee')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    context = {'form' : form, 'msg' : msg}
    return render(request, 'new_login.html', context)


def admin(request):
    return render(request,'admin.html')


def customer(request):
    return render(request,'customer.html')


def employee(request):
    return render(request,'employee.html')


def view_admins(request):
    users = User.objects.all()
    print(users)
    return render(request, 'view_admins.html', {'users': users})

def view_customers(request):
    customers = Cliente.objects.all()
    print(customers)
    return render(request, 'view_customers.html', {'customers' : customers})

def edit_customer(request, customer_id):
    customer = get_object_or_404(Cliente, id=customer_id)
    form = CustomerForm(request.POST or None, instance=customer)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('users:view_customers')
    context = {'form' : form, 'customer' : customer}
    return render(request, 'edit_customer.html', context)

def delete_customer(request, customer_id):
    customer = get_object_or_404(Cliente, id=customer_id)

    if request.method == 'POST':
        customer.delete()
        return redirect('users:view_customers')
    context = {'customer' : customer}
    return render(request, 'delete_customer.html', context)

def view_customer(request, customer_id):
    customer = get_object_or_404(Cliente, id = customer_id)
    context = {'customer' : customer}
    return render(request, 'view_customer.html', context)