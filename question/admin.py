from django.contrib import admin
from .models import *

class question_dataAdmin(admin.ModelAdmin):
	list_display=["q_id","q_name","q_question","q_type","q_max_time","q_max_memory"]

admin.site.register(question_data, question_dataAdmin)

# Register your models here.
