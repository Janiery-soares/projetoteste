from django.contrib import admin
from .models import Produto
from .models import Cliente
from .models import DadosPessoal

admin.site.register(Produto)
admin.site.register(Cliente)
admin.site.register(DadosPessoal)
