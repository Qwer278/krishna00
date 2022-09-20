from django.contrib import admin
from service.model import hosting ,room,msg

class serviceAdmin(admin.ModelAdmin):
    list_display=('room_id','host1','host2')

class ipadmin(admin.ModelAdmin):
    list_display=('status','pub_date','ip')

class msgadmin(admin.ModelAdmin):
    list_display=('room_id','message')


admin.site.register(room,serviceAdmin)
admin.site.register(hosting,ipadmin)
admin.site.register(msg,msgadmin)