
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def redirect_to_login(request):
    return redirect('instrucao:login_usuario')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('instrucao/', include(('instrucao.urls', 'instrucao'), namespace='instrucao')),
    #path('', lambda request: redirect('instrucao/', permanent=False)),
    path('', redirect_to_login),

    
]
    