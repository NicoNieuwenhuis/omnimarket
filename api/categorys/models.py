from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Category(MPTTModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=40)
    description = models.TextField(blank=True, null=True)
    parent = TreeForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children', )
    pricetype = models.ManyToManyField('pricetype.Pricetype', related_name="catpricetype", blank=True)

    def get_family_tree(self):
        return self.name


    class MPTTMeta:
        db_table = "categories"
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

def get_all_children(self, include_self=True):
    return Category.objects.filter(self.get_children_filters(include_self))


