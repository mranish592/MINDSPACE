
from django.urls import path, include
from mindspace_app import views,urls

app_name = 'mindspace_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.ActivityCreateView.as_view(), name='create'),
    path('update/<pk>', views.ActivityUpdateView.as_view(), name='update'),
    path('delete/<pk>', views.ActivityDeleteView.as_view(), name='delete'),
    path('detail/<pk>', views.ActivityDetailView.as_view(), name='detail'),

]
