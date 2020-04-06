from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import CustomUserCreationForm
from .models import WaferUser, Account, Customer, Wafer

# Create your views here.

class HelloWorld(TemplateView):
	template_name = 'test.html'

class WafersView(LoginRequiredMixin, ListView):
    model = Wafer
    template_name = 'index.html'
    login_url = 'login'

    # def get_queryset(self):
    #     current_user = self.request.user
    #     following = set()
    #     for conn in UserConnection.objects.filter(creator=current_user).select_related('following'):
    #         following.add(conn.following)
    #     return Post.objects.filter(author__in=following)

class WaferDetailView(LoginRequiredMixin, DetailView):
    model = Wafer
    template_name = 'wafer_detail.html'

class WaferCreateView(LoginRequiredMixin, CreateView):
    model = Wafer
    template_name = 'wafer_create.html'
    fields = '__all__'
    login_url = 'login'

class WaferUpdateView(UpdateView):
    model = Wafer
    template_name = 'wafer_update.html'
    fields = '__all__'

class WaferDeleteView(DeleteView):
    model = Wafer
    template_name = 'wafer_delete.html'
    success_url = reverse_lazy("wafers")

class Signup(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy("login")

class UserDetailView(DetailView):
    model = WaferUser
    template_name = 'user_detail.html'
    login_url = 'login'

class EditProfile(LoginRequiredMixin, UpdateView):
    model = WaferUser
    template_name = 'edit_profile.html'
    fields = ['profile_pic', 'username']
    login_url = 'login'