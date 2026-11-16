from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from core.forms import DonationForm

def home(request):
    if request.method == "POST":
        return render(request, 'personalized.html')
    return render(request, 'home.html')

def menu(request):
    return render(request, 'menu.html')

def cei_7_ani(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            
            return render(request, 'cei_7_ani_success.html', {'form': form})
    else:
        form = DonationForm()
    return render(request, 'cei_7_ani.html', {'form': form})

def traducerea_autorilor(request):
    return render(request, 'traducerea_autorilor.html')

def lecturi_usoare(request):
    return render(request, 'lecturi_usoare.html')

def cartea_saptamanii(request):
    
    return render(request, 'cartea_saptamanii.html')

def proiecte_educativ_culturale(request):
    return render(request, 'proiecte_educativ_culturale.html')

def libraria_coresi(request):
    return render(request, 'libraria_coresi.html')

def cine_a_fost_coresi(request):
    return render(request, 'cine_a_fost_coresi.html')

def evaluare_manuscrise(request):
    return render(request, 'evaluare_manuscrise.html')

def vreau_sa_public(request):
    return render(request, 'vreau_sa_public.html')

def contact(request):
    return render(request, 'contact.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def adevaruri_ascunse(request):
    return render(request, 'adevaruri_ascunse.html')  

def detalii_program(request):
    return render(request, 'detalii_program.html')

def sa_vorbim_corect_romaneste(request):
    return render(request, 'sa_vorbim_corect_romaneste.html')
