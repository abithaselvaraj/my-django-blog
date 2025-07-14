from django.db import models
from django.utils.text import slugify   # ✅ used to generate slugs from text


class Category(models.Model):
    name = models.CharField(max_length=50)  # Category name like 'Tech', 'Health', etc.

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image_url = models.URLField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # 🔥 NEW FIELD
    # slug = models.SlugField(unique=True)  
    slug = models.SlugField(blank=True, null=True,unique=True)  # no `unique=True`

# NEW LINE:
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name="posts",
        default=1
    )

    def __1str__(self):
        return self.title

    # 🔁 OVERRIDE SAVE METHOD TO AUTO-GENERATE SLUG
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # 🚀 convert title to slug before saving
        super(Post, self).save(*args, **kwargs)


