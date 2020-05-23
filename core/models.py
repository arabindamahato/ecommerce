from django.conf import settings
from django.db import models

CATEGORY_CHOICES = (
    ('S', 'Shirt'),
    ('SW', 'Sport Wear'),
    ('OW', 'Out wear'),
)

LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger'),
)


class Item(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField()
    category = models.CharField(
        choices=CATEGORY_CHOICES, max_length=2, default="S")
    label = models.CharField(choices=LABEL_CHOICES, max_length=1, default="P")

    def __str__(self):
        return self.title


class OrderItem(models.Model):
    item = models.ForeignKey(Item, models.CASCADE)

    def __str__(self):
        return self.item


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
