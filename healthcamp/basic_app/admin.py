from django.contrib import admin
from basic_app.models import Person,Village,Journal,JournalEntries,Campain,Staff

# Register your models here.
admin.site.register(Person)
admin.site.register(Village)
admin.site.register(Journal)
admin.site.register(JournalEntries)
admin.site.register(Campain)
admin.site.register(Staff)
