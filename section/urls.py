from django.urls import path
from section.views import (
    SectionListView,
    SectionDetailView,
    #SectionCreateView,
)

urlpatterns = [
    path("", SectionListView.as_view(), name="list_section"),
    path("<int:pk>/", SectionDetailView.as_view(), name="show_section"),
    #path("create/", SectionCreateView.as_view(), name="create_section"),
]
