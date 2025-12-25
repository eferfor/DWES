from django.contrib import admin
from .models import Efecto, Ingrediente, Especialidad, Aquelarre, Bruja, Cliente, Pocion, Pedido, PocionesPedido

# Register your models here.
admin.site.register(Efecto)
admin.site.register(Especialidad)
admin.site.register(Ingrediente)
admin.site.register(Aquelarre)
admin.site.register(Bruja)
admin.site.register(Cliente)
admin.site.register(PocionesPedido)


class PocionesPedidoInline(admin.TabularInline):
    model = PocionesPedido
    extra = 1
    autocomplete_fields = ['pocion']
    fields = ['pocion', 'cantidad', 'precio_unidad']

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'fecha', 'precio_total']
    inlines = [PocionesPedidoInline]

@admin.register(Pocion)
class PocionAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'tamano', 'bruja']
    search_fields = ['nombre']