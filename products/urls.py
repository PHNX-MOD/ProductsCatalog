from django.urls import path
from . import views
from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from .views import ProductViewSet, CategoryViewSet
from .views import ProductListView, ProductDetailView, ProductUpdateView, ProductDeleteView, ProductCreateView, CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDetailView, CategoryDeleteView, search

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('about/',views.about, name='about'),
    url(r'^s/', search, name='search'),
    path('list/', ProductListView.as_view(), name='products_list'),
    path('detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('category_list/', CategoryListView.as_view(), name='category_list'),
    path('category_create/', CategoryCreateView.as_view(), name='category_create'),
    path('category_update/<int:pk>', CategoryUpdateView.as_view(), name='category_update'),
    path('category_detail/<int:pk>', CategoryDetailView.as_view(), name='category_detail'),
    path('category_delete/<int:pk>', CategoryDeleteView.as_view(), name='category_delete'),
    path('', include(router.urls)),
    path('rest-api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/v1/categories/(?P<pk>[0-9]+)$',views.get_delete_update_category,name='get_delete_update_category'),
    url(r'^api/v1/categories/$', views.get_post_categories, name='get_post_categories'),
]