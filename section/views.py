from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
import random
from django.shortcuts import render
from clothe.models import Clothe

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

class OutfitListView(LoginRequiredMixin, ListView):
    model = Section
    template_name = "section/ootd.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        items = list(Clothe.objects.all())
        random_item = random.choice(items)
        context['topper']= random_item.image

        # nulist = []
        # for clothing in Section.objects.all():
        #     for item in Clothe.objects.all():
        #         if item.id == clothing.id:
        #             pass
        # context['stuff'] = nulist

        toplist = []
        pantlist = []
        shoelist = []
        for clothings in Clothe.objects.all():
            if clothings.section_id == 1 and clothings.is_laundry == 0:
                toplist.append(clothings)
            elif clothings.section_id == 2 and clothings.is_laundry == 0:
                pantlist.append(clothings)
            elif clothings.section_id == 3 and clothings.is_laundry == 0:
                shoelist.append(clothings)

        context['top']  = random.choice(toplist)
        context['pant'] = random.choice(pantlist)
        context['shoe'] = random.choice(shoelist)

        return context

        

    def get_queryset(self):
        return Section.objects.filter(owner=self.request.user)
