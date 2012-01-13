from django.contrib.gis.db import models


class Zipcode(models.Model):
    code = models.CharField(max_length=5, db_index=True)
    mpoly = models.MultiPolygonField()

    objects = models.GeoManager()

    def __unicode__(self):
        return self.code

    class Meta:
        ordering = ['code']


class State(models.Model):
    fips_code = models.CharField('FIPS Code', max_length=2)
    usps_code = models.CharField('USPS state abbreviation', max_length=2, db_index=True)
    name = models.CharField(max_length=100, db_index=True)
    area_description_code = models.CharField(max_length=2)
    feature_class_code = models.CharField(max_length=5)
    functional_status = models.CharField(max_length=1)
    mpoly = models.MultiPolygonField()

    objects = models.GeoManager()

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']


class County(models.Model):
    state_fips_code = models.CharField('State FIPS Code', max_length='2')
    fips_code = models.CharField('FIPS Code', max_length=3)
    county_identifier = models.CharField(max_length=5)
    name = models.CharField(max_length=100)
    name_and_description = models.CharField(max_length=100)
    legal_statistical_description = models.CharField(max_length=2)
    fips_55_class_code = models.CharField(max_length=2)
    feature_class_code = models.CharField(max_length=5)
    functional_status = models.CharField(max_length=1)
    mpoly = models.MultiPolygonField()

    objects = models.GeoManager()

    def state(self):
        my_state = State.objects.get(fips_code=self.state_fips_code)
        return my_state

    class Meta:
        verbose_name_plural = 'Counties'

    def __unicode__(self):
        return self.name
