from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_blog_posts'] = ['fee', 'fi', 'fo', 'phum']
        return context
