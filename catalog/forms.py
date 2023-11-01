from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        #fields = '__all__' (взаимоисключающие друг друга поля (3 варианта))
        fields = ('title', 'description', 'image', 'category', 'price')
        #exclude = ('date_of_change')

    def clean_title(self):
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        cleaned_data = self.cleaned_data['title']

        for i in forbidden_words:
            if i == cleaned_data:
                raise forms.ValidationError('Невозможно создать продукт с таким названием')

        return cleaned_data


class ProductFormModerator(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        #fields = '__all__' (взаимоисключающие друг друга поля (3 варианта))
        fields = ('description', 'category')
        #exclude = ('date_of_change')

    def clean_title(self):
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        cleaned_data = self.cleaned_data['title']

        for i in forbidden_words:
            if i == cleaned_data:
                raise forms.ValidationError('Невозможно создать продукт с таким названием')

        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'
