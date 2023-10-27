from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    #fields = ('title', 'description', 'image', 'category', 'price') убираем, так как используем джанго формс
    success_url = reverse_lazy('catalog:homepage')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    #fields = ('title', 'description', 'image', 'category', 'price')
    #success_url = reverse_lazy('catalog:list') убираем, так как метод переопределен ниже

    def get_success_url(self):
        return reverse('catalog:product', args=[self.kwargs.get('pk')])


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/homepage.html'

""" FBV:
def homepage(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Главная'
    }
    return render(request, 'catalog/homepage.html', context)
"""


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'

""" FBV:
def product(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        'object': product,
        'title': 'Продукт',
    }
    return render(request, 'catalog/product.html', context)
"""


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:homepage')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name}, {phone} - {message}')

    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)
