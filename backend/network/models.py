from django.db import models


class Network(models.Model):

    SYSTEM = 1
    PUBLIC = 2
    PRIVATE = 3
    ALLOCATION_CHOICES = (
        (SYSTEM, 'System'),
        (PUBLIC, 'Public'),
        (PRIVATE, 'Private'),
    )

    v4 = 4
    v6 = 6
    VERSION_CHOICES = (
        (v4, 'v4'),
        (v6, 'v6'),
    )

    allocation = models.IntegerField(
        default=PUBLIC,
    )

    network = models.GenericIPAddressField()

    prefix = models.IntegerField()

    version = models.IntegerField(
        default=v4,
        choices=VERSION_CHOICES,
    )

    is_active = models.BooleanField(
        default=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    is_deleted = models.BooleanField(
        default=False
    )

    deleted_at = models.DateTimeField(
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ['-id']
        verbose_name = "Network"
        verbose_name_plural = "Networks"

    def __unicode__(self):
        return '%s/%s' % (self.network, self.prefix)
