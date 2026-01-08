from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.indexViews.as_view()),
    path('foundation/', views.foundationViews.as_view()),
    path('lita_prueba/', views.ModeloPruebaListView.as_view()),
    path('addd/', views.PruebaCreateView.as_view(), name='prueba_add'),

]

