from django.contrib import admin
from .models import Curso, Carrera, Categoria

# Register your models here.

class CursoAdmin(admin.ModelAdmin):
    readonly_fields = ('creado','actualizado')
class CarreraAdmin(admin.ModelAdmin):
    readonly_fields = ('creado','actualizado')

admin.site.register(Curso, CursoAdmin)
admin.site.register(Carrera, CarreraAdmin)
admin.site.register(Categoria)

