from django.contrib import admin
from .models import Job,Node,M_to_M,Skillset,Resource,Tool

# Register your models here.
admin.site.register(Job)
admin.site.register(Node)
admin.site.register(M_to_M)
admin.site.register(Skillset)
admin.site.register(Resource)
admin.site.register(Tool)