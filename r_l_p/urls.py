from django.conf.urls import url
from r_l_p import views
# SET THE NAMESPACE!
app_name = 'r_l_p'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]