from django.contrib import admin

from .models import Screen, LaptopModel, CPU, RAM, Storage, GPU, Laptop

admin.site.register(Screen)
admin.site.register(LaptopModel)
admin.site.register(CPU)
admin.site.register(RAM)
admin.site.register(Storage)
admin.site.register(GPU)
admin.site.register(Laptop)
