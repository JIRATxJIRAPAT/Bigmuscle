from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views import View
from django.views.generic.edit import UpdateView, DeleteView
from .models import Post, Comment
from social.forms import PostForm, CommentForm
from Users.models import *
from django.shortcuts import get_object_or_404
from Trainer.models import *
from django.http import HttpResponseRedirect
from django.urls import reverse


class PostListView(View):
    def get(self, request, *args, **kwargs):
        try:
            checkTr = Trainer.objects.get(user=request.user)
        except Trainer.DoesNotExist:
            checkTr = None

        if checkTr is not None:
            return HttpResponseRedirect(reverse("Trainer:index"))
        else:
            customer_ex= get_object_or_404(Customer,pk=request.user.customer.id)
            print(customer_ex)
            posts = customer_ex.my_post.all().order_by('-created_on')
        
            form = PostForm()

            context = {
                'post_list': posts,
                'form': form,
            }
            return render(request, 'social/post_list.html', context)

    def post(self, request, *args, **kwargs):
        try:
            checkTr = Trainer.objects.get(user=request.user)
        except Trainer.DoesNotExist:
            checkTr = None

        if checkTr is not None:
            return HttpResponseRedirect(reverse("Trainer:index"))
        else:
            customer_ex= get_object_or_404(Customer,pk=request.user.customer.id)
            print(customer_ex)
            posts = customer_ex.my_post.all().order_by('-created_on')
            form = PostForm(request.POST)
            if form.is_valid():
                print("add success")
                new_post = form.save(commit=False)
                new_post.author = request.user
                new_post.for_author = request.user.customer
                new_post.save()

            context = {
                'post_list': posts,
                'form': form,
            }
            return render(request, 'social/post_list.html', context)

class PostDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        
        post = Post.objects.get(pk=pk)
        form = CommentForm()
        comments = Comment.objects.filter(post=post).order_by('-created_on')
        context = {
            'post': post,
            'form': form,
            'comments': comments,
            
        }
        print("dddddaaashere")

        return render(request, 'social/post_detail.html', context)

    def post(self, request,pk, *args, **kwargs):
        print("ddddd")
        post = Post.objects.get(pk=pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.save()
        
        comments = Comment.objects.filter(post=post).order_by('-created_on')

        context = {
            'post': post,
            'form': form,
            'comments': comments,
        }

        return render(request, 'social/post_detail.html', context)

class PostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    print("edit this")
    model = Post
    fields = ['body']
    template_name = 'social/post_edit.html'
    
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('social:post-detail', kwargs={'pk': pk})
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'social/post_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'social/comment_delete.html'

    def get_success_url(self):
        pk = self.kwargs['post_pk']
        return reverse_lazy('post-detail', kwargs={'pk': pk})

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author