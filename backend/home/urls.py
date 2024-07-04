from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('predict/', views.predict, name='predict'),
    path('analysis/', views.analysis, name='analysis'),
    path('api/student', views.StudentListCreateView.as_view() ),
    path('api/student/<int:pk>', views.StudentDetailView.as_view() ),
]