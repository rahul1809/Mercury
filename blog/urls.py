from django.urls import path

from . import views

# https://​docs.​djangoproject.​com/​en/​2.​0/​topics/​http/​urls/​#path-​converters.
# https:/​/​docs.​djangoproject.​com/​en/2.​0/​ref/​urls/​#django.​urls.​re_​path

# application namespace
app_name = 'blog'
urlpatterns = [

    # post views
    path('', views.PostListView.as_view(), name='post_list'),
    path('tag/<slug:tag_slug>/', views.PostListView.as_view(), name='post_list_by_tag'),
    path('<int:year>/<str:month>/<int:day>/<slug>/', views.PostDateDetailView.as_view(),
         name='post_detail_by_date_slug'),

]
