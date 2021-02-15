from django.contrib import admin

from .models import Produto, Usuario


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Usuario, UsuarioAdmin)
