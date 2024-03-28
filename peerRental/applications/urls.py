from django.urls import path
import applications.views as av

urlpatterns = [
    path('productapplications/<str:prod_id>O<int:sell_id>',av.applicationsreq,name='applicationsreq'),
    path('applicationdetails/<str:prod_id>B<int:buy_id>S<int:sell_id>',av.applicationdetails,name='applicationdetails'),
    path('accept/<str:prod_id>A<int:buy_id>',av.acceptapp,name='acceptapp'),
    path('reject/<str:prod_id>R<int:buy_id>',av.rejectapp,name='rejectapp'),
    path('myorders/<int:id>',av.myorders,name='myorders'),
    path('applicationedit/<str:prod_id>A<int:buy_id>',av.applicationedits,name='applicationedits'),
]