"""
Definition of urls for DjangoWebProject1.
"""

                      ############ Django project ############
                      
                      
                      #### mysite

from django.contrib import admin
from django.urls import path, include
from register import views as v
#from . import views


urlpatterns = [
    path('admin', admin.site.urls),
    path("register/", v.register, name="register" ),
    path('', include("main.urls")),
    path('', include("django.contrib.auth.urls")),
    ]



# urlpatterns = [
#     path('', views.home, name='home'),
#     path('contact/', views.contact, name='contact'),
#     path('about/', views.about, name='about'),
#     path('login/',
#          LoginView.as_view
#          (
#              template_name='app/login.html',
#              authentication_form=forms.BootstrapAuthenticationForm,
#              extra_context=
#              {
#                  'title': 'Log in',
#                  'year' : datetime.now().year,
#              }
#          ),
#          name='login'),
#     path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
#     path('admin/', admin.site.urls),
# ]
