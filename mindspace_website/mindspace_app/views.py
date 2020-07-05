from django.shortcuts import render
from mindspace_app.models import *
from django.http import HttpResponse
from django.views.generic import View, TemplateView,CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.
class IndexView(TemplateView):
    template_name = 'mindspace_app/index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        activities = Activity.objects.all()
        context={'activities':activities}
        return context

class ActivityCreateView(CreateView):
    fields = ('heading','status','percentage')
    model = Activity

class ActivityUpdateView(UpdateView):
    fields = ('heading','status','percentage')
    model = Activity

class ActivityDeleteView(DeleteView):
    model = Activity
    success_url = reverse_lazy("mindspace_app:index")
