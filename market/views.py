from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from .models import Post, Comment, ReviewRating
from django.http import HttpResponseRedirect
from .forms import CommentForm, ReviewForm
from django.contrib import messages


def index(request):
    """ a view to retuern the index page """

    return render(request, 'market/index.html')


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'market/market.html'
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        return render(
            request,
            "market/post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.comment = post
            comment.save()
            messages.success(request, 'You have successfully added a Comment')
        else:
            comment_form = CommentForm()
            messages.info(request,
                          'Oops! somthing wasnt right there,\
                            make sure you are logged and try again!')

        return render(
            request,
            "market/post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": comment_form
            },
        )


class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            messages.info(request,
                          'Sorry you didnt love this as much as we do!')
        else:
            post.likes.add(request.user)
            messages.success(request, 'We loved this too!')
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def submit_review(request, post_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            reviews = ReviewRating.objects.get(user__id=request.user.id,
                                               post__id=post_id)
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            return redirect(url)
        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.post_id = post_id
                data.user_id = request.user.id
                data.save()
                return redirect(url)
