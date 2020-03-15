from django.db import models
import datetime
class profile(models.Model):
    name = models.CharField(        max_length=32, null=False, blank=True)
    surname = models.CharField(     max_length=32, null=False, blank=True)
    phone_number = models.CharField(max_length=10, null=False, blank=True)
    mail = models.CharField(        max_length=32, null=False, blank=True)
    address = models.CharField(     max_length=48, null=False, blank=True)
    def _str_(self):
        return self._surname + ' ' + self._name
    # def get_abs_url(self):
        # return reverse("profiler-gc:profiler", kwargs = {"slug":self.slug})
