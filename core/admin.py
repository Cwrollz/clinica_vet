from django.contrib import admin
from .models import Tutor, Animal, Veterinario, Especialidade, Consulta, Prontuario

admin.site.register(Tutor)
admin.site.register(Animal)
admin.site.register(Veterinario)
admin.site.register(Especialidade)
admin.site.register(Consulta)
admin.site.register(Prontuario)