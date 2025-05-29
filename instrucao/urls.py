from django.urls import path
from . import views

urlpatterns = [
   #path('rh_instrucao/', views.rh_instrucao, name="rh_instrucao"),
   # path('teste/', views.teste, name="teste"),
   path('design', views.design, name="design"),
   path('', views.instrucao, name="pagina_principal"),
   path('instrucao/buscar', views.instrucao, name="instrucao"),

   # Rotas do Formulario
   path('coletar_dados_caminhao_forms/', views.caminhaoFormsdados, name='coletar_dados_caminhao_forms'),
   path('coletar_dados_trator_forms/',views.tratorFormsdados, name='coletar_dados_trator_forms'),
   path('coletar_dados_colhedora_forms/',views.colhedoraFormsdados, name='coletar_dados_colhedora_forms'),
   path('coletar_dados_lider_forms/',views.LiderFormdados, name='coletar_dados_lider_forms'),

   #Rota mensagen
   path('sucesso/',views.sucesso, name="sucesso"),
   path('erro/',views.erro, name="erro"),

   #Rota De busca
   path('buscar/', views.BuscarGeral, name='buscar_geral'),
  
]