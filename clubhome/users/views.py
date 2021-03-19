from django.contrib.auth import get_user_model
from django.views.generic import TemplateView, DetailView

User = get_user_model()


class UserProfileGenericView(DetailView):
    model = User
    slug_field = 'username'
    slug_url_kwarg = 'username'


class UserProfileView(TemplateView):
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        profile_user = User.objects.get(username=kwargs.get('username'))

        context['profile_picture'] = profile_user.profile_picture
        context['name'] = profile_user.name
        context['username'] = profile_user.username
        context['profile_description'] = profile_user.profile_description
        context['twitter'] = profile_user.twitter
        context['instagram'] = profile_user.instagram

        return context
