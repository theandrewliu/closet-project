from django.urls import path
from clothe.views import ClotheCreateView, ClotheListView, ClotheUpdateView,ClotheDeleteView

urlpatterns = [
    path("create/", ClotheCreateView.as_view(), name="create_clothe"),
    path("mine/", ClotheListView.as_view(), name="show_my_clothe"),
    path("<int:pk>/complete/", ClotheUpdateView.as_view(), name="complete_clothe"),
    path("<int:pk>/delete/", ClotheDeleteView.as_view(), name="delete_clothe"),
    # path("ootd/", OutfitList, name="ootd"),
]