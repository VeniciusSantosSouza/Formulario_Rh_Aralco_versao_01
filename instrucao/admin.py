# instrucao/admin.py

from django.contrib import admin
from .models import Caminhao
from .models import Trator
from .models import Colhedora
from .models import Lider

admin.site.register(Caminhao)
admin.site.register(Trator)
admin.site.register(Colhedora)
admin.site.register(Lider)
