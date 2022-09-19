from django.contrib import admin
from service.model import hosting ,room,msg
# Register your models here.
# @admin.register(service)
# @admin.register(hosting)
# @admin.register()
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
class serviceAdmin(admin.ModelAdmin):
    list_display=['room_id','host1','host2']

class ipadmin(admin.ModelAdmin):
    list_display=['status','pub_date','ip']

class msgadmin(admin.ModelAdmin):
    list_display=['room_id','message']

class UserAdmin(AuthUserAdmin):
    create_form_class = UserCreationForm
    # add_form = MyUserCreationForm
    update_form_class = UserChangeForm


admin.site.register(User, UserAdmin)

admin.site.register(room,serviceAdmin)
admin.site.register(hosting,ipadmin)
admin.site.register(msg,msgadmin)