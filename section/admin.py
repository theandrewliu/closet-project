from django.contrib import admin

from section.models import(
    Section
)

from clothe.models import(
    Clothe
)
# Register your models here.

class SectionAdmin(admin.ModelAdmin):
    pass

class ClotheAdmin(admin.ModelAdmin):
    pass

admin.site.register(Section, SectionAdmin)
admin.site.register(Clothe, ClotheAdmin)