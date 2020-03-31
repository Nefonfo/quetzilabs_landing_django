from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import OurOffer

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request, *args, **kwargs):
        data = OurOffer.objects.all()

        return render(request, self.template_name, {
            'css_files': (
                'core/assets/css/index/index.css',
            ),
            'js_files': (
                'core/assets/js/index/typing-letter.js',
            ),
            'our_offers': data
        })
