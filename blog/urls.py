from django.urls import path
from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path("detail/", views.detail, name="detail"),
    # path("post/<int:post_id>/", views.detail, name="post_detail"),
    #to expect text instead of numbers,use:
    # path("post/<str:post_id>/", views.detail, name="post_string"),

    path("old-url/", views.old_url_redirect, name="old_url"),
    # commenting for names url
    # path("new-url/", views.new_url, name="new_url"),

    path("new-url/", views.new_url, name="new_page"),

    #template rendering
    #commenting to demonstrate home.html template rendering layout
    # path("", views.index, name="index"),
    
    # path('', views.home_view, name='home'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),        
    #commenting to demonstrate pagination
    #path('', views.all_posts, name='all_posts'),  # home page shows all posts

    # path('post/<int:post_id>/', views.post_detail, name='post'),
    path('price/', views.price_view, name='price'),
    path('post/<slug:slug>/', views.post_detail_by_slug, name='post_by_slug'),

    #pagination example
    path('', views.index, name='index') , # Home page
    path('contact/', views.contact_view, name='contact'),

]

