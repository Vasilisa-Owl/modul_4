from django.urls import path
from .views import index, top_sellers, login, advertisement, advertisement_post, profile, register

urlpatterns = [path('', index, name='index'),
               path('top-sellers/', top_sellers, name='top-sellers'),
               path('login/', login, name='login'),
               path('advertisement/', advertisement, name='advertisement'),
               path('advertisement_post/', advertisement_post, name='advertisement-post'),
               path('profile/', profile, name='profile'),
               path('register/', register, name='register'),]