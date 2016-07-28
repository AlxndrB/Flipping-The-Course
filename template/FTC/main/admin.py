from django.contrib import admin
<<<<<<< HEAD
from main.models import UserProfile, Modules, Questions

admin.site.register(UserProfile)
admin.site.register(Modules)
admin.site.register(Questions)
=======
from main.models import UserProfile, Questions, Modules

admin.site.register(UserProfile)
admin.site.register(Questions)
admin.site.register(Modules)
>>>>>>> master
