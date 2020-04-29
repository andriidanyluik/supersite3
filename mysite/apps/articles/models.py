import datetime
from django.db import models
from django.utils import timezone

class Article_AD(models.Model):
	article_title = models.CharField('Назва статті', max_length = 200 )
	article_text = models.TextField('Текст статті')
	pub_date = models.DateTimeField('Дата публікації')

	def __str__(self):
		return self.article_title
	class Meta:
		verbose_name = 'Стаття Адміністрування'
		verbose_name_plural = 'Статті Адміністрування'

class Article_PG(models.Model):
	article_title = models.CharField('Назва статті', max_length = 200 )
	article_text = models.TextField('Текст статті')
	pub_date = models.DateTimeField('Дата публікації')
	def __str__(self):
		return self.article_title

	class Meta:
		verbose_name = 'Стаття Програмування'
		verbose_name_plural = 'Статті Програмування'
class Comment_AD(models.Model):
	comment_ad = models.ForeignKey(Article_AD, on_delete = models.CASCADE)
	author_name = models.CharField("Ім'я автора", max_length = 200)
	comment_text = models.CharField("Текст коментаря", max_length =200)
	def __str__(self):
		return self.author_name

	class Meta:
		verbose_name = 'Коментар Адміністрування'
		verbose_name_plural = 'Коментарі Адміністрування'
class Comment_PG(models.Model):
	comment_pg = models.ForeignKey(Article_PG, on_delete = models.CASCADE)
	author_name = models.CharField("Ім'я автора", max_length = 50)
	comment_text = models.CharField("Текст коментаря", max_length =200)
	def __str__(self):
		return self.author_name
	class Meta:
		verbose_name = 'Коментар Програмування'
		verbose_name_plural = 'Коментарі Програмування'