from django.db import models


class UserMessage(models.Model):
    name = models.CharField(max_length=155, verbose_name='Имя')
    email = models.EmailField(verbose_name='Почта')
    subject = models.CharField(max_length=155, verbose_name='Тема')
    message = models.TextField(verbose_name='Сообщение')
    
    def __str__(self) -> str:
        return f'{self.name} {self.email} {self.subject}'
    
    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        
        
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    
    def __str__(self) -> str:
        return self.name
    

class Projects(models.Model):
    name = models.CharField(max_length=125, verbose_name='Имя')
    description = models.CharField(max_length=155, verbose_name='Описание')
    link = models.URLField(verbose_name='Ссылка')
    image = models.ImageField(upload_to='project_image/', verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категорий')
    
    def __str__(self) -> str:
        return f'{self.name} {self.link}'
    
    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
