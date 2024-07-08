from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(paciente)
admin.site.register(medico)
admin.site.register(consulta)
admin.site.register(prescricao)
admin.site.register(medicamento)
