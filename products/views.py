from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

from django.shortcuts import render
from django.urls import reverse_lazy
from rest_framework import viewsets
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

def home(request):
    return render(request, 'products/home.html')

def about(request):
    return render(request, 'products/about.html', {'title': 'About'})

def search(request):
    try:
        s = request.GET.get('s')
    except:
        s = None
    if  s:
        products = Product.objects.filter(name__icontains=s)
        context = {'query': s, 'products': products}
        template = 'products/search.html'
    else:
        template = 'products/products.html'
        context = {}
    return render(request, template, context)



class ProductListView(ListView):
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'products/product_update.html'
    context_object_name = 'product'
    fields = '__all__'
    success_url = reverse_lazy('products_list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/product_delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('products_list')


class ProductCreateView(CreateView):
    model = Product
    template_name = 'products/product_create.html'
    fields = '__all__'
    success_url = reverse_lazy('products_list')

class CategoryListView(ListView):
    model = Category
    template_name = 'products/category_list.html'
    context_object_name = 'categories'

class CategoryCreateView(CreateView):
    model = Category
    template_name = 'products/category_create.html'
    fields = '__all__'
    success_url = reverse_lazy('category_list')

class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'products/category_update.html'
    fields = ['name']
    context_object_name = 'category'
    fields = '__all__'
    success_url = reverse_lazy('category_list')

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'products/category_detail.html'
    context_object_name = 'category'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = context['category']
        products = Product.objects.filter(category=category)
        context['products'] = products
        return context

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'products/category_delete.html'
    context_object_name = 'categories'
    success_url = reverse_lazy('category_list')

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_category(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response({})
    elif request.method == 'DELETE':
        return Response({})
    elif request.method == 'PUT':
        return Response({})

@api_view(['GET', 'POST'])
def get_post_categories(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        return Response({})
