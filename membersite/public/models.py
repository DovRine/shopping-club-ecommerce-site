from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to="products", default="default.png")
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    likes = models.PositiveIntegerField(default=0)
    description = models.TextField()

    @property
    def cart_link(self):
        return '#'

    @property
    def detail_link(self):
        return '#'

    @property
    def short_description(self):
        return self.description

    def __str__(self):
        return f'{self.title}'
    
    def __repr__(self):
        return f'Product(title={self.title}, description={self.description})'