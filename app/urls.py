from . import views
from django.urls import path
app_name="app"
urlpatterns=[
    path("",views.hello),
    # path('search/', views.SearchView.as_view(), name='search'),
]    