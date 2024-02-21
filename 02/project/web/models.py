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


class Author(models.Model):
    name = models.CharField(
        verbose_name="Name",
        max_length=100,
        blank=False,
    )

    def __str__(self):
        return "{}".format(self.name)


class Book(models.Model):
    name = models.CharField(
        verbose_name="Name",
        max_length=100,
        blank=False,
    )
    author = models.ForeignKey(
        Author,
        verbose_name="Author",
        blank=False,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "{} / {}".format(self.name, self.author)


class Edition(models.Model):
    name = models.CharField(
        verbose_name="Name",
        max_length=100,
        blank=False,
    )
    book = models.ForeignKey(
        Book,
        verbose_name="Book",
        blank=False,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "{} / {}".format(self.name, self.book)
