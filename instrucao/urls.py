from django.urls import path
from . import views

urlpatterns = [
   #path('rh_instrucao/', views.rh_instrucao, name="rh_instrucao"),
   # path('teste/', views.teste, name="teste"),
   path('design', views.design, name="design"),
   path('instrucao/', views.instrucao, name="instrucao"),
   path('instrucao/buscar', views.instrucao, name="instrucao"),
   path('coletar_dados_caminhao_forms/', views.caminhaoFormsdados, name='coletar_dados_caminhao_forms'),
   path('coletar_dados_trator_forms/',views.tratorFormsdados, name='coletar_dados_trator_forms'),
   path('coletar_dados_colhedora_forms/',views.colhedoraFormsdados, name='coletar_dados_colhedora_forms'),
   path('coletar_dados_trator_forms/',views.tratorFormsdados, name='coletar_dados_trator_forms'),
   path('coletar_dados_lider_forms/',views.LiderFormdados, name='coletar_dados_lider_forms'),

]