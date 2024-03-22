from django.urls import path
import core.views as cv

urlpatterns = [
    path('',cv.home,name='home'),
    path('delete/<str:prod_id>',cv.delete_prod,name='delete_prod'),
    path('rent/<str:prod_id>',cv.rent_prod,name='rent_prod'),
    path('rentprod/<str:prod_id>B<int:buy_id>S<int:sell_id>',cv.complete_order,name='complete_order'),
    path('clearchats/<str:prod_id>B<int:from_id>S<int:to_id>',cv.clearchats,name='clearchats'),
    path('confirm_rent/<str:prod_id>B<int:buy_id>S<int:sell_id>',cv.confirm_rent,name='confirm_rent'),
    path('myproducts/<str:id>',cv.myproducts,name='myproducts'),
]