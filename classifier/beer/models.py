from django.db import models

# Create your models here.
class Styles(models.Model):
    name = models.CharField(max_length=200)
    ibu_min = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    ibu_max = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    srm_min = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    srm_max = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    og_min = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    og_max = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    fg_min = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    fg_max = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    abv_min = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    abv_max = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    objects = models.Manager()