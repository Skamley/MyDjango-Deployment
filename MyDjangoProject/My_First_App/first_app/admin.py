from django.contrib import admin
from first_app.models import  AccessRecord, Topic, WebPage,Access_Record,Employee, UserProfileInfo



# Register your models here.

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(WebPage)
admin.site.register(Access_Record)
admin.site.register(Employee)
admin.site.register(UserProfileInfo)
