from django.db import models

# Create your models here.


# 书籍表
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pub_date = models.DateField()
    authors = models.ManyToManyField(to='Author')
    publisher = models.ForeignKey(to='Publisher', on_delete=models.CASCADE)
    
    
# 出版社表
class Publisher(models.Model):
    name = models.CharField(max_length=48)
    addr = models.TextField()

    def __str__(self):
        return self.name
    
    
# 作者表
class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.SmallIntegerField()
    detail = models.OneToOneField(to='AuthorDetail', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

# 作者详情表
class AuthorDetail(models.Model):
    gender_choices = (
        (0, '女'),
        (1, '男'),
        (2, '保密'),
    )
    gender = models.SmallIntegerField(choices=gender_choices)
    phone = models.CharField(max_length=32)
    info = models.TextField
