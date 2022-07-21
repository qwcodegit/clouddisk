from django.db import models

# Create your models here.

class fileMo(models.Model):
    id=models.AutoField(primary_key=True,verbose_name="ID")
    name=models.CharField(max_length=114514,verbose_name="文件名")
    file=models.FileField(upload_to="userfile",verbose_name="文件")
    time=models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    class Meta:
        verbose_name='文件'
        verbose_name_plural=verbose_name
        def __str__(self):
            return self.name