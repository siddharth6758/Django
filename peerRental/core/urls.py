from django.urls import path
import core.views as cv

urlpatterns = [
    path('',cv.home,name='home'),
    path('delete/<str:prod_id>',cv.delete_prod,name='delete_prod'),
    path('rent/<str:prod_id>',cv.rent_prod,name='rent_prod'),
]