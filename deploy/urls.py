from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from deploy import views

urlpatterns = [
    url(r'^artifacts/(?P<pk>[0-9]+)/$', views.ArtifactDetail.as_view()),
    url(r'^artifacts/$', views.ArtifactList.as_view()),
    url(r'^manifests/(?P<pk>[0-9]+)/$', views.ManifestDetail.as_view()),
    url(r'^manifests/$', views.ManifestList.as_view()),
    url(r'^updates/(?P<pk>[0-9]+)/$', views.UpdateDetail.as_view()),
    url(r'^updates/$', views.UpdateList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
