from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('info/', views.info, name='info'),
    path('<int:pk>/info/', views.DetailInfo.as_view(), name='info'),
    path('testowytemplate', views.testowytemplate, name='testowytemplate'),
]

urlpatterns += staticfiles_urlpatterns()
