from django.urls import path
import core.views as cv

urlpatterns = [
    path('',cv.home,name='home'),
]