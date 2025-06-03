import os
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
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
from django.db.models import Q

@login_required
def erro(request):
    return render(request, 'instrucao/erro.html')

@login_required
def sucesso(request):
    return render(request, 'instrucao/sucesso.html')

#@login_required
#def instrucao(request):
    #return render(request, 'instrucao/rh_instrucao.html')

#def teste(request):
   # return render(request, 'instrucao/teste.html')

# Criei uma (função) para recerber os dados do html
@login_required # Só pessoas logada tem acesso a essa funsões
def caminhaoFormsdados(request):
    if request.method == 'POST':
        form = CaminhaoForm(request.POST) 
        print("POST recebido:", request.POST) 
        if form.is_valid(): 
            form.save()
            print("Formulário válido, salvando...")
            return render(request, 'instrucao/sucesso.html')
        else:
            print("Formulario inválido, NÃO salvou nada.")
            print(form.errors)
            
            return render(request, 'instrucao/erro.html')
    else:
        form = CaminhaoForm()
        return render(request, 'instrucao/rh_instrucao.html',{'form': form})


@login_required
def tratorFormsdados(request):
    if request.method == 'POST':
        form = TratorForm(request.POST)
        print("POST recebido:", request.POST)
        if form.is_valid():
            dados = form.cleaned_data
            form.save() 
            return render(request, 'instrucao/sucesso.html')
        else:
            print("Formulário inválido, NÃO salvou nada.")
            print(form.errors)
            
            return render(request, 'instrucao/erro.html')
    else:
        form = TratorForm()
        return render(request, 'instrucao/rh_instrucao.html', {'form': form})


@login_required
def colhedoraFormsdados(request):
    if request.method == 'POST':
        form = ColhedoraForm(request.POST)
        print("POST recebido:", request.POST)
        if form.is_valid():        
            form.save()
            return render(request, 'instrucao/sucesso.html')
        else:
            print("Formulário inválido, NÃO salvou nada.")
            print(form.errors) 

            return render(request, 'instrucao/erro.html')
    else:
        form = ColhedoraForm()
        return render(request, 'instrucao/rh_instrucao.html', {'form' : form})

@login_required
def LiderFormdados(request):
    if request.method == 'POST':
        form = LiderForm(request. POST)
        print("POST recebido:", request.POST)
        if form.is_valid():
            dados = form.cleaned_data
            form.save()
            return render(request, 'instrucao/sucesso.html')
        else:
            print("Formulario inválido, NÃO salvou nada.")
            print(form.errors)

            return render(request, 'instrucao/erro.html')
    else:
        form = LiderForm()
        return render(request, 'instrucao/rh_instrucao.html',{'form' : form})


@login_required
def BuscarGeral(request):
    query = request.GET.get('buscar', '')
    tipo = request.GET.get('tipo', '')

    caminhao_resultados = []
    colhedora_resultados = []
    trator_resultados = []
    lider_resultados = []

    if tipo == 'caminhao' or tipo == '':
        if query:
            caminhao_resultados = Caminhao.objects.filter(
                Q(data_caminhao__icontains=query) |
                Q(hora_caminhao__icontains=query) |
                Q(matricula_instrutor_caminhao__icontains=query) |
                Q(nome_instrutor_caminhao__icontains=query) |
                Q(matricula_condutor_caminhao__icontains=query) |
                Q(nome_condutor_caminhao__icontains=query) |
                Q(equipamento_caminhao__icontains=query) |
                Q(local_saida_caminhao__icontains=query) |
                Q(hora_saida_caminhao__icontains=query) |
                Q(km_saida_caminhao__icontains=query) |
                Q(local_chegada_caminhao__icontains=query) |
                Q(hora_chegada_caminhao__icontains=query) |
                Q(km_chegada_caminhao__icontains=query) |
                Q(viagem_caminhao__icontains=query) |
                Q(media_caminhao__icontains=query) |
                Q(avaliacao_op_mantenedor_caminhao__icontains=query) |
                Q(avaliacao_digitacao_bordo_caminhao__icontains=query) |
                Q(acoes_autorizadas_caminhao__icontains=query) |
                Q(operacao_caminhao__icontains=query) |
                Q(avaliacao_caminhao__icontains=query) |
                Q(observacoes__icontains=query)
            )
        else:
            caminhao_resultados = Caminhao.objects.all()

    if tipo == 'colhedora' or tipo == '':
        if query:
            colhedora_resultados = Colhedora.objects.filter(
                Q(matricula_condutor_colhedora__icontains=query) |
                Q(nome_condutor_colhedora__icontains=query) |
                Q(equipamento_colhedora__icontains=query) |
                Q(hora_saida_colhedora__icontains=query) |
                Q(hora_chegada_colhedora__icontains=query) |
                Q(horimetro_inicial_colhedora__icontains=query) |
                Q(horimetro_final_colhedora__icontains=query) |
                Q(frente_colhedora__icontains=query) |
                Q(avaliacao_operacao_mantendedor_colhedora__icontains=query) |
                Q(avaliacao_digitacao_bordo_colhedora__icontains=query) |
                Q(avaliacao_acoes_autorizadas_colhedora__icontains=query) |
                Q(avaliacao_operacao_colhedora__icontains=query) |
                Q(avaliacao_pressao_corte_base_colhedora__icontains=query) |
                Q(avaliacao_pressao_picador_colhedora__icontains=query) |
                Q(avaliacao_configuracao_cb_colhedora__icontains=query) |
                Q(avaliacao_sincronismo_transbordo_colhedora__icontains=query) |
                Q(avaliacao_velocidade_constante_colhedora__icontains=query) |
                Q(avaliacao_utilizacao_tecnologia_colhedora__icontains=query) |
                Q(avaliacao_senso_de_dono_colhedora__icontains=query) |
                Q(avaliacao_geral_instrutor_colhedora__icontains=query) |
                Q(observacoes__icontains=query)
            )
        else:
            colhedora_resultados = Colhedora.objects.all()

    if tipo == 'trator' or tipo == '':
        if query:
            trator_resultados = Trator.objects.filter(
                Q(data_trator__icontains=query) |
                Q(hora_trator__icontains=query) |
                Q(matricula_instrutor_trator__icontains=query) |
                Q(nome_instrutor_trator__icontains=query) |
                Q(matricula_condutor_trator__icontains=query) |
                Q(nome_condutor_trator__icontains=query) |
                Q(equipamento_trator__icontains=query) |
                Q(local_saida_trator__icontains=query) |
                Q(hora_saida_trator__icontains=query) |
                Q(local_chegada_trator__icontains=query) |
                Q(hora_chegada_trator__icontains=query) |
                Q(horimetro_inicial_trator__icontains=query) |
                Q(horimetro_final_trator__icontains=query) |
                Q(avaliacao_operador_mantenedor_trator__icontains=query) |
                Q(avaliacao_digitacao_bordo_trator__icontains=query) |
                Q(avaliacao_acoes_autorizadas_trator__icontains=query) |
                Q(avaliacao_operacao_trator__icontains=query) |
                Q(avaliacao_instrutor_trator__icontains=query) |
                Q(avaliacao_rotacoes_trator__icontains=query) |
                Q(avaliacao_senso_dono_trator__icontains=query) |
                Q(avaliacao_troca_marcha_trator__icontains=query) |
                Q(avaliacao_troca_embreagem_trator__icontains=query) |
                Q(avaliacao_velocidade_constante_trator__icontains=query) |
                Q(avaliacao_sincronismo_colheora_trator__icontains=query) |
                Q(avaliacao_paralelismo_trator__icontains=query) |
                Q(observacoes__icontains=query)
            )
        else:
            trator_resultados = Trator.objects.all()

    if tipo == 'lider' or tipo == '':
        if query:
            lider_resultados = Lider.objects.filter(
                Q(data_lider__icontains=query) |
                Q(hora_lider__icontains=query) |
                Q(matricula_instrutor_lider__icontains=query) |
                Q(nome_instrutor_lider__icontains=query) |
                Q(matricula_do_lider__icontains=query) |
                Q(nome_do_lider__icontains=query) |
                Q(frente_lider__icontains=query) |
                Q(fazenda_lider__icontains=query) |
                Q(unidade_lider__icontains=query) |
                Q(avaliacao_organizacao_area_trasnbordamento_lider__icontains=query) |
                Q(avaliacao_abertura_aceiros_lider__icontains=query) |
                Q(avaliacao_tempo_carregamento_metros_lineares_lider__icontains=query) |
                Q(avaliacao_qualidade_colheita_lider__icontains=query) |
                Q(avaliacao_aproveitamento_tempo_colhedora__icontains=query) |
                Q(avaliacao_lideranca_equipe__icontains=query) |
                Q(avaliacao_final_instrutor__icontains=query) |
                Q(observacoes__icontains=query)
            )
        else:
            lider_resultados = Lider.objects.all()

    context = {
        'query': query,
        'tipo': tipo,
        'caminhao_resultados': caminhao_resultados,
        'colhedora_resultados': colhedora_resultados,
        'trator_resultados': trator_resultados,
        'lider_resultados': lider_resultados,
    }

    return render(request, 'resultado_busca_geral.html', context)

@login_required
def instrucao(request):
    FUNCIONARIO = {
        "35037": "Venicius",
        "38028": "Bryan",
        "39040": "Joselita",
        "36060": "Uéverson",
        "10010": "Gleyci",
        "30148": "Lehh",
        
    }

    INSTRUTOR = {
        "10011": "Robinho",
        "20011": "Tiago",
        "30011": "PBenjamin Franklin",
    }

    return render(request, 'instrucao/rh_instrucao.html', {
        'funcionario': FUNCIONARIO,
        'instrutor': INSTRUTOR,
        })  



@staff_member_required
def editar_caminhao(request, id):
    caminhao = get_object_or_404(Caminhao, id_caminhao=id) 
    if request.method == 'POST':
        form = CaminhaoForm(request.POST, instance=caminhao)
        if form.is_valid():
            form.save()
            return render(request, 'instrucao/sucesso.html')

        else:
            print("Formulário inválido, NÃO salvou nada.")
            print(form.errors)
            
            return render(request, 'instrucao/erro.html')
    else:
        form = CaminhaoForm(instance=caminhao)

    return render(request, 'instrucao/editar_formulario.html', {'form': form})



@staff_member_required
def editar_colhedora(request, id):
    colhedora = get_object_or_404(Colhedora, id_colhedora=id)
    if request.method == 'POST':
        form = ColhedoraForm(request.POST, instance=colhedora)
        if form.is_valid():
            form.save()
            return render(request, 'instrucao/sucesso.html')

        else:
            print("Formulário inválido, NÃO salvou nada.")
            print(form.errors)

            return render(request, 'instrucao/erro.html')
        
    else:
        form = ColhedoraForm(instance=colhedora)
    return render(request, 'instrucao/editar_formulario.html', {'form': form})



@staff_member_required
def editar_trator(request, id):
    trator = get_object_or_404(Trator, id_trator=id)
    if request.method == 'POST':
        form = TratorForm(request.POST, instance=trator)
        if form.is_valid():
            form.save()
            return render(request,'instrucao/sucesso.html')
        
        else:
            return render (request, 'instrucao/erro.html')

    else:
        form = TratorForm(instance=trator)
    return render(request, 'instrucao/editar_formulario.html', {'form': form})



@staff_member_required
def editar_lider(request, id):
    lider = get_object_or_404(Lider, id_lider=id)
    if request.method == 'POST':
        form = LiderForm(request.POST, instance=lider)
        if form.is_valid():
            form.save()
            return render(request, 'instrucao/sucesso.html')
        else:
            return render (request, 'instrucao/erro.html')
    else:
        form = LiderForm(instance=lider)
    return render(request, 'instrucao/editar_formulario.html', {'form': form})



def login_usuario(request):

    if request.user.is_authenticated: #Se estiver logado retornar pra pagina inicial
        return redirect('instrucao:pagina_principal')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect('instrucao:pagina_principal')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    else:
        form = AuthenticationForm()

    return render(request, 'instrucao/login.html', {'form': form})


@login_required
def logout_usuario(request):
    logout(request)
    messages.success(request,"Você saiu da sua conta com sucesso.")
    return redirect('instrucao:login_usuario')