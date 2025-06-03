from django.urls import path
from . import views
from .views import login_usuario


app_name = 'instrucao'


urlpatterns = [
   #path('rh_instrucao/', views.rh_instrucao, name="rh_instrucao"),
   # path('teste/', views.teste, name="teste"),
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

   #Rota de preencher automatico
   path('meus-funcionarios/', views.instrucao, name='meus_funcionarios'),


   #Rota de edição
   path('editar/caminhao/<int:id>/', views.editar_caminhao, name='editar_caminhao'),
   path('editar/colhedora/<int:id>',views.editar_colhedora, name='editar_colhedora'),
   path('editar/trator/<int:id>/', views.editar_trator, name='editar_trator'),
   path('editar/lider/<int:id>/', views.editar_lider, name='editar_lider'),  

   #Rota de Login
   path('login_usuario', views.login_usuario, name='login_usuario'),
   path('logout/', views.logout_usuario, name='logout_usuario'),
   
]