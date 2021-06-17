
from django.urls import path
from . import views
urlpatterns = [
 path('student/',views.studentDetail.as_view(),name='studentDetail')
]
