from django.conf.urls import url
from app import views


urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^login/$', views.auth_user, name="login"),
    url(r'^pricing/$', views.pricing, name="pricing"),
    url(r'^signup/$', views.register, name="signup"),
    url(r'^profile/$', views.profile, name="profile"),

    

]
