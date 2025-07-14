from django.core.management.base import BaseCommand
from blog.models import Category

class Command(BaseCommand):
    help = 'Populates the Category table with default values'

    def handle(self, *args, **kwargs):
        # Clear existing categories
        Category.objects.all().delete()

        # Predefined list of categories
        categories = ['Sports', 'Technology', 'Science', 'Art', 'Food']

        for name in categories:
            Category.objects.create(name=name)

        self.stdout.write(self.style.SUCCESS("✅ Successfully populated categories!"))
