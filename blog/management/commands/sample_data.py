from django.core.management.base import BaseCommand
from blog.models import Post
from blog.models import Category
import random
class Command(BaseCommand):
    help = 'Seeds the database with sample blog post data.'

    def handle(self, *args, **kwargs):
        Post.objects.all().delete()
        # categories = Category.objects.all().delete();

        titles = [
            "First Post", "Second Thoughts", "Tech Trends", "My Django Journey",
            "Startup Life", "Meditation and Code", "AI for Beginners"
        ]
        contents = [
            "This is the first blog post.", "Here's something worth reading...",
            "Welcome to my thoughts on tech!", "Django is awesome!",
            "Startup stories are wild!", "Balance is important.", "LLMs are evolving fast!"
        ]
        image_urls = [
            f"https://picsum.photos/id/{i}/640/400" for i in range(20, 27)
        ]

        # fetches categories from the database
        categories=Category.objects.all()

        for title, content, image in zip(titles, contents, image_urls,):
            category=random.choice(categories) 
            Post.objects.create(title=title, content=content, image_url=image,category=category)

        self.stdout.write(self.style.SUCCESS("✅ Sample blog posts inserted!"))
