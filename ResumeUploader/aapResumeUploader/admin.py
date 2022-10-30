from django.contrib import admin
from .models import Resume

# Register your models here.

# register to admin
# admin.site.register(Resume)
# or

@admin.register(Resume)
class ResumeModelAdmin(admin.ModelAdmin):
    # fields = ['name', 'dob']
    list_display = ['id','name', 'dob','gender','locality','city','pin','state','mobile','email','job_city','profile_image','my_file']
