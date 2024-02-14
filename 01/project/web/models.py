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
    rating = models.PositiveIntegerField(
        verbose_name="Rating (1-5)",
        blank=False,
    )


class ReviewDetail(models.Model):
    review = models.ForeignKey(
        Review,
        verbose_name="Review",
        blank=False,
        on_delete=models.CASCADE,
    )
    detail = models.TextField(
        verbose_name="Detail",
        blank=False,
    )
