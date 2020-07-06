from django.shortcuts import render
from mindspace_app.models import *
from django.http import HttpResponse
from django.views.generic import (
        View, TemplateView,CreateView,
        UpdateView, DeleteView,
        DetailView, ListView,
)
from django.urls import reverse_lazy
# Create your views here.
class IndexView(TemplateView):
    template_name = 'mindspace_app/index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        activities = Activity.objects.all()
        context={'activities':activities}
        return context

class ActivityDetailView(DetailView):
    context_object_name = 'activity_detail'
    model = Activity
    template_name = 'mindspace_app/activity_detail.html'

class ActivityCreateView(CreateView):
    fields = ('heading','status','percentage','description')
    model = Activity

class ActivityUpdateView(UpdateView):
    fields = ('heading','status','percentage','description')
    model = Activity

class ActivityDeleteView(DeleteView):
    model = Activity
    success_url = reverse_lazy("mindspace_app:index")
