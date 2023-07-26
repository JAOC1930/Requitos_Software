from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User

class MyCustomView(LoginRequiredMixin, TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context