from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (ListView,
		 DetailView,
		 CreateView,
		 UpdateView,
		 DeleteView,
		 View)
from .models import post
from users.forms import CommentForm

# Create your views here.

def home(request):
	context = {
		'posts':  post.objects.all()

	}
	return render(request, 'blog/home.html' , context)

class PostListView(ListView):
	model = post
	template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	paginate_by = 5

class UserPostListView(ListView):
	model = post
	template_name = 'blog/user_posts.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
	model = post

class PostCreateView(LoginRequiredMixin, CreateView):
	model = post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
	model = post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
	model = post
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

def about(request):
	return render(request, 'blog/about.html')


class FrontendRenderView(View):
	def get(self, request, *args, **kwargs):
		return render(request, "pages/home.html", {})

def add_comment_to_post(request, pk):
    posts = get_object_or_404(post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = posts
            comment.save()
            return redirect('post-detail', pk=posts.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})