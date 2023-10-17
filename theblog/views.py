from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post,Category,Comment
from .forms import PostForm,EditForm,CommentForm
from django.urls import reverse_lazy, reverse

#def home(request):
 #   return HttpResponse(request, 'home.html',{})

class HomeView(ListView):
    model = Post
    template_name="home.html"
    ordering=['post_date']

    def get_context_data(self,*args,**kwargs):
          cat_menu=Category.objects.all()
          context=super(HomeView,self).get_context_data(*args,**kwargs)
          context["cat_menu"] =cat_menu
          return context


def LikeView(request,pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked=False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked=False
    else:
        post.likes.add(request.user)
        liked=True
    return HttpResponseRedirect(reverse('article_detail',args=[str(pk)]))




def CategoryView(request,cats):
    category_posts=Post.objects.filter(category__iexact=cats.title().replace('-',' '))
    return render(request,'categories.html',{'cats':cats.title().replace('-',' '), 'category_posts':category_posts})

class ArticleDetailsView(DetailView):
    model = Post
    template_name="articles_details.html"

    def get_context_data(self,*args,**kwargs):
          cat_menu=Category.objects.all()
          context=super(ArticleDetailsView,self).get_context_data(*args,**kwargs)
           
          stuff=get_object_or_404(Post,id=self.kwargs['pk'])
          total_likes=stuff.total_likes()

          liked=False
          if stuff.likes.filter(id=self.request.user.id).exists():
            liked=True
          context["cat_menu"] = cat_menu
          context["total_likes"]=total_likes
          context["liked"] = liked
          return context

class AddPostsView(CreateView):
    model=Post
    form_class= PostForm
    template_name="add_posts.html"
   # fields="__all__"

class AddCommentView(CreateView):
    model=Comment
    form_class= CommentForm
    template_name="add_comment.html"
    success_url=reverse_lazy('home')

    def form_valid(self, form):
        form.instance.post_id=self.kwargs['pk']
        return super().form_valid(form)


class AddCategoryView(CreateView):
    model=Category
    template_name="add_category.html"
    fields='__all__'

class UpdatePostView(UpdateView):
    model=Post
    form_class= EditForm
    template_name="update_post.html"
    #fields=["title","title_tag","body"]

class DeletePostView(DeleteView):
    model=Post
    template_name="delete_post.html"
    #fields=["title","title_tag","body"]
    success_url=reverse_lazy('home')






















    
 

