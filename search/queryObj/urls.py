from django.urls import path
from . import views

urlpatterns = [
    path('', views.ssearch, name='search'),
    path('reports_list', views.reports_list, name='reports_list'),
    # path('search_by_q_objects', views.search_by_q_objects, name="search_by_q_objects"),
    path('search_by_q_objects', views.RecommendationsChecksRanSearch.as_view(), name="search_by_q_objects")
]