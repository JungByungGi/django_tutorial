from django.contrib import admin
from .models import Board


# Register your models here.

class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', ) # model class field list up


admin.site.register(Board, BoardAdmin)
