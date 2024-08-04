//project
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
   path('admin/', admin.site.urls),
   path('',include("prob1.urls")),
   #path('',include("prob2.urls")),
   #path('',include("prob3.urls")),
   #path('',include("prob4.urls")),
