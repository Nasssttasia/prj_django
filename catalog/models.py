from django.db import models


NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    description = models.CharField(max_length=300, verbose_name='описание')
    image = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)  # необязательное поле
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    price = models.IntegerField()
    date_of_creation = models.DateField(**NULLABLE)
    date_of_change = models.DateField(**NULLABLE)

    def __str__(self):
        return f'{self.title}'

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


class Version(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    number = models.IntegerField(verbose_name='номер версии')
    title = models.CharField(max_length=100, verbose_name='название версии')
    is_active = models.BooleanField(default=True, verbose_name='версия активна')



    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
        ordering = ('title',)

