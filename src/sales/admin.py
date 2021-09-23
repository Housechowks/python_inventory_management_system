from django.contrib import admin

from .models import CSV, Position, Sale


admin.site.register(Position)
admin.site.register(CSV)
admin.site.register(Sale)