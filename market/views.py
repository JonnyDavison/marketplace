from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post, Comment, Rating
from django.http import JsonResponse


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
                "liked": liked
            },
        )


def rating_view(request):
    rating = Rating.objects.filter(rating=0).first()
    context = {
        'rating': rating
    }
    return render(request, 'market/market.html', context)


def rateing_value(request):
    if request.method == 'POST':
        rate_id = request.POST.get('rate_id')
        rate_value = request.POST.get('rate_value')
        rating = Rating.objects.get(id=rate_id)
        rating.score = rate_value
        rating.save()
        return JsonResponse({'success': 'true', 'rating': rate_value}, safe=False)
    return JsonResponse({'success': 'false'})
