from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Mahsulot nomi")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Narxi (so'm)")
    image = models.ImageField(upload_to='products/', verbose_name="Rasm")
    description = models.TextField(verbose_name="Tavsif", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
