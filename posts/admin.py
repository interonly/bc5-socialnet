from django.contrib import admin
from .models import *


admin.site.register(Publication)
admin.site.register(Like)
admin.site.register(Dislike)