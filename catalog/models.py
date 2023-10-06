from django.db import models


NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    description = models.CharField(max_length=300, verbose_name='описание')
    image = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)  # необязательное поле
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    price = models.IntegerField()
    date_of_creation = models.DateField()
    date_of_change = models.DateField()

    def __str__(self):
        return f'{self.title}, {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('title',)


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('title',)


