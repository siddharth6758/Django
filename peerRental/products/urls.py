from django.urls import path
import products.views as pv

urlpatterns = [
    path('uploadproduct/',pv.upload_prod,name='upload'),
    path('myproducts/edit/<str:prod_id>x<int:id>',pv.edit_prod,name='edit'),
]