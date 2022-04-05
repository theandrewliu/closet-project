from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Clothe
from django.urls import reverse_lazy
from django.views.generic.list import ListView

# Create your views here.


class ClotheCreateView(LoginRequiredMixin, CreateView):
    model = Clothe
    template_name = "clothe/create.html"
    fields = []

    def get_success_url(self):
        return reverse_lazy("show_section", args=[self.object.project.id])


class ClotheListView(LoginRequiredMixin, ListView):
    model = Clothe
    template_name = "clothe/list.html"

    def get_queryset(self):
        return Clothe.objects.filter(owner=self.request.user)


class ClotheUpdateView(LoginRequiredMixin, UpdateView):
    model = Clothe
    fields = ["is_laundry"]

    def get_success_url(self):
        return reverse_lazy("show_my_clothe")
