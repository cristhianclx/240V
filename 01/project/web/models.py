from django.db import models


class Review(models.Model):
    name = models.CharField(
        verbose_name="Name (person that is doing a review)",
        max_length=100,
        blank=False,
    )
    review = models.TextField(
        verbose_name="Review",
        blank=False,
    )