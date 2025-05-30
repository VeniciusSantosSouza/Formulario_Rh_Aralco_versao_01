
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('instrucao/', include(('instrucao.urls', 'instrucao'), namespace='instrucao')),
    path('', lambda request: redirect('instrucao/', permanent=False)),

    
]
    