from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version


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

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version,form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
            
        return super().form_valid(form)


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['version'] = Version.objects.all()
        return context

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
