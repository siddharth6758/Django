from django.urls import path
import products.views as pv

urlpatterns = [
    path('uploadproduct/',pv.upload_prod,name='upload'),
    path('myproducts/edit/<str:prod_id>X<int:id>',pv.edit_prod,name='edit'),
    path('myproducts/chatwith/<str:prod_id>W<int:id>',pv.chatwith,name='chatwith'),
]