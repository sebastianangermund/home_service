from django.shortcuts import render
from .models import LedLightData


class DataListView(LoginRequiredMixin, generic.ListView):
    model = LedLightData
    template_name = 'analytics/led_list.html'
    paginate_by = 10
