import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import CaminhaoForm
from .forms import TratorForm
from .forms import ColhedoraForm
from .forms import LiderForm
from .models import Caminhao
from .models import Trator
from .models import Colhedora
from .models import Lider



def instrucao(request):
    return render(request, 'instrucao/rh_instrucao.html')

#def teste(request):
   # return render(request, 'instrucao/teste.html')

def design(request):
   return render(request, 'static/css/design.css')

   #from django.shortcuts import render



# Criei uma (função) para recerber os dados do html
def caminhaoFormsdados(request):
    if request.method == 'POST':
        form = CaminhaoForm(request.POST) 
        print("POST recebido:", request.POST) 
        if form.is_valid(): 
            print("Formulário válido, salvando...")
            return HttpResponse("Dados salvos com sucesso!")
        else:
                print("Formulário inválido, NÃO salvando nada.")
                print(form.errors)
                return render(request, 'instrucao/rh_instrucao.html',{'form': form})



def tratorFormsdados(request):
    if request.method == 'POST':
        form = TratorForm(request.POST)
        print("POST recebido:", request.POST)
        if form.is_valid():
            dados = form.cleaned_data
            form.save() 
            return HttpResponse("Dados salvos com sucesso!")
        else:
            return render(request, 'instrucao/rh_instrucao.html',{'form': form})
    else:
        form = TratorForm()
        return render(request, 'instrucao/rh_instrucao.html', {'form': form})

def colhedoraFormsdados(request):
    if request.method == 'POST':
        form = ColhedoraForm(request.POST)
        print("POST recebido:", request.POST)
        if form.is_valid():
            dados = form.cleaned_data
            form.save()
            return HttpResponse("Dados salvos com sucesso !")
        else:
            return render(request, 'instrucao/rh_instrucao.html', {'form': form})
    else:
        form = ColhedoraForm()
        return render(request, 'instrucao/rh_instrucao.html', {'form' : form})

#Aqui esta rodando

def LiderFormdados(request):
    if request.method == 'POST':
        form = LiderForm(request. POST)
        print("POST recebido:", request.POST)
        if form.is_valid():
            dados = form.cleaned_data
            form.save()
            #return redirect('resultlider')
            return HttpResponse("Dados salvos com sucesso !")
        else:
            return render(request, 'instrucao/rh_instrucao.html', {'form' : form})
    else:
        form = LiderForm()
        return render(request, 'instrucao/rh_instrucao.html',{'form' : form})







