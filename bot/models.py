from django.db import models

# Create your models here.

class Profile(models.Model):
	tg_id = models.PositiveIntegerField(verbose_name='TG ID')
	username = models.CharField(max_length=200, verbose_name='Имя пользователя', blank=True, null=True)
	first_name = models.CharField(max_length=200, verbose_name='Имя', blank=True, null=True)
	last_name = models.CharField(max_length=200, verbose_name='Имя', blank=True, null=True)

	class Meta:
		verbose_name = 'Профиль'
		verbose_name_plural = 'Профили'

	def __str__(self):
		return str(self.tg_id)

class FAQ(models.Model):
	question = models.CharField(max_length=400, verbose_name='Вопрос')
	answer = models.TextField(verbose_name='Ответ')

	class Meta:
		verbose_name = 'Вопрос/ответ'
		verbose_name_plural = 'Вопросы/ответы'

	def __str__(self):
		return self.question

class Cat(models.Model):
	image = models.ImageField(upload_to='cats', verbose_name='Изображение')

	class Meta:
		verbose_name = 'Фото кота'
		verbose_name_plural = 'Фото котов'

	def __str__(self):
		return str(self.id)