from django.urls import path
import userAuthenticate.views as uav

urlpatterns = [
    path('login/',uav.login_user,name='login'),
    path('signup/',uav.signup,name='signup'),
    path('signup/',uav.signup,name='signup'),
    path('logout/',uav.logout_user,name='logout'),
    path('adminpanel/',uav.adminpage,name='adminpage'),
    path('user/<int:id>',uav.userhome,name='userhome'),
]