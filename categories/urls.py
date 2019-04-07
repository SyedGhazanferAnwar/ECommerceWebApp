from django.urls import path
from . import views

app_name="main"

urlpatterns = [
    #path('admin/', admin.site.urls),
    path("",views.homepage,name="homepage"),
    path('Category',views.Category,name="Category")

]
