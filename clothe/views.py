from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Clothe
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, CreateView
from django.shortcuts import render
import random
# Create your views here.


class ClotheCreateView(LoginRequiredMixin, CreateView):
    model = Clothe
    template_name = "clothe/create.html"
    fields = ["name","image","section"]

    def get_success_url(self):
        return reverse_lazy("list_section") #args=[self.object.id])


class ClotheListView(LoginRequiredMixin, ListView):
    model = Clothe
    template_name = "clothe/list.html"

    def get_queryset(self):
        return Clothe.objects.filter(owner=self.request.user)


class ClotheUpdateView(LoginRequiredMixin, UpdateView):
    model = Clothe
    fields = ["is_laundry"]

    def get_success_url(self):
        return reverse_lazy("home")

class ClotheDeleteView(LoginRequiredMixin, DeleteView):
    model = Clothe
    template_name="clothe/delete.html"
    success_url = reverse_lazy("home")

# def OutfitList(request):
#     Outfit = list(Clothe.objects.all())

#     Outfit = random.sample(Outfit,1)

#     return render(request, 'section/ootd.html', {'Outfit': Outfit})