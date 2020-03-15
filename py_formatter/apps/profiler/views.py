from django.shortcuts import render
from django.views.generic import ListView
from .models import profile

class indexView(ListView):
    from .models import profile
    template_name = 'profiler/main.html'
    def get_queryset(self):
        return profile.objects.all()

def main(request):
    context = {}
    return render(request, 'profiler/main.html', context)
    
