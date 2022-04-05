from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from .models import Section



# Create your views here.
class SectionListView(LoginRequiredMixin, ListView):
    model = Section
    template_name = "section/list.html"

    def get_queryset(self):
        return Section.objects.filter(owner=self.request.user)

class SectionDetailView(LoginRequiredMixin, DetailView):
    model = Section
    template_name = "section/detail.html"

# class ProjectCreateView(LoginRequiredMixin, CreateView):
#     model = Project
#     template_name = "projects/create.html"
#     fields = ["name", "description", "members"]

#     def get_success_url(self):
#         return reverse_lazy("show_project", args=[self.object.id])
