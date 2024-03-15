from django.urls import path
import core.views as cv
import userAuthenticate.views as uav

urlpatterns = [
    path('',cv.home,name='home'),
]