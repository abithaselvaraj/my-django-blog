from django.shortcuts import render,redirect

from django.urls import reverse

# Create your views here.
from django.http import HttpResponse
from django.core.paginator import Paginator


# commenting to demonstrate index.html template rendering
""" 
def index(request):
    return HttpResponse("Hello World! You are at blog index.")
 """

""" from django.shortcuts import render

def index(request):
    return render(request, "blog/index.html") """

""" 

def detail(request):
    return HttpResponse("Post detail page")
 """

def detail(request, post_id):
    return HttpResponse(f"Viewing Post ID: {post_id}")


""" 
#commenting to demonstrate reverse 
def old_url_redirect(request):
    return redirect("new_url") """

def new_url(request):
    return HttpResponse("This is the new URL")

def old_url_redirect(request):
    return redirect(reverse("blog:new_page"))

#commenting to show pass context to template
""" def home_view(request):
    return render(request, 'blog/home.html') """


def home_view(request):
    context = {
        'name': 'krishna',
        'age': 'infinite',
    }
    return render(request, 'blog/home.html', context)

#commenting to demonstrate post_detail with logging handler
""" def post_detail(request,id):
    posts = [
        {'title': 'Post 1'},
        {'title': 'Post 2'},
        {'title': 'Post 3'},
    ]
    return render(request, 'blog/blog.html', {'posts': posts}) """


def price_view(request):
    context = {'price': 400}
    return render(request, 'blog/price.html', context)



from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)  # Create logger for this file/module

#gets static data from a list of dictionaries
""" def post_detail(request, post_id):
    posts = [
    {
        "id": 1,
        "title": "Django Introduction",
        "content": "Django is a high-level Python Web framework.",
        "image_url": "https://example.com/images/django1.png"
    },
    {
        "id": 2,
        "title": "Understanding Views",
        "content": "Views are Python functions that return responses.",
        "image_url": "https://example.com/images/views.png"
    },
    {
        "id": 3,
        "title": "Routing in Django",
        "content": "URL patterns connect URLs to views in Django.",
        "image_url": "https://example.com/images/routing.png"
    }
]

    post = next((item for item in posts if item["id"] == int(post_id)), None)
    
    logger.debug(f"Post variable is: {post}")  # Logs the retrieved post (or None)

    return render(request, "blog/post_detail.html", {"post": post}) """

# Gets posts from the database using Django ORM
from django.shortcuts import render, get_object_or_404
from .models import Post

def post_detail(request, id):

    post = get_object_or_404(Post, pk=id)
    related_posts = Post.objects.filter(category=post.category).exclude(id=post.id)[:3]

    return render(request, 'blog/post_detail.html', {'post': post, 'related_posts': related_posts})




from django.shortcuts import render
from .models import Post  # import the Post model (DB table)

def all_posts(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, "blog/all_posts.html", {"posts": posts})


from django.shortcuts import get_object_or_404, render
from .models import Post

def post_detail_by_slug(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post_detail.html", {"post": post})


from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post

def index(request):
    all_posts = Post.objects.all().order_by('created_at')  # Fetch all blog posts
    paginator = Paginator(all_posts, 2)  # Show 5 posts per page

    page_number = request.GET.get("page")  # Get page number from URL
    page_obj = paginator.get_page(page_number)  # Get the page object

    return render(request, 'blog/index.html', {'page_obj': page_obj})



from django.shortcuts import render
from .forms import ContactForm
import logging

logger = logging.getLogger(__name__)

def contact_view(request):
    form = ContactForm()
    success_message = None  # ✅ Start fresh every time

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            logger.info(f"Contact Form Data: {name}, {email}, {message}")
            success_message = f"Message from {name} sent successfully!"
            form = ContactForm()  # Reset form
        else:
            logger.info("Form validation failed.")
            success_message = None  # Force-clear it here

            # No need to reset success_message because it's already None

    return render(request, 'blog/contact.html', {
        'form': form,
        'success_message': success_message
    })
