from django.views.generic.base import TemplateView
from .models import BlogPost

class BlogView(TemplateView):
    template_name = "blog_post.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = BlogPost.objects.filter(slug=self.kwargs['slug']).first()
        return context
