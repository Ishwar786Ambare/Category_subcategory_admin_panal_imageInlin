from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, related_name='souscatégories', on_delete=models.CASCADE)
    name = models.CharField(max_length=150, db_index=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    category = models.ForeignKey(Category, related_name='produits', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, related_name='produits', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image/',null=True,blank=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    pimage = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image/',null=True,blank=True)

    def __str__(self):
        return self.pimage.name
