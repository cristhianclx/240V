from django.db import models


class Document(models.Model):
    document = models.FileField(
        upload_to="documents",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )


class DocumentMatch(models.Model):
    document = models.ForeignKey(
        Document,
        on_delete=models.CASCADE,
    )
    position = models.CharField(
        max_length=255,
        blank=False,
    )
    ranking = models.DecimalField(
        max_digits=35,
        decimal_places=30,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
