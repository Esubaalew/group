from django.contrib import admin
from .models import FocusField, Member

class FocusFieldInline(admin.TabularInline):
    model = Member.focus_fields.through

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
   list_display = ['first_name', 'last_name']
   inlines = [FocusFieldInline]
@admin.register(FocusField)
class FocusFieldAdmin(admin.ModelAdmin):
    list_display = ['name']