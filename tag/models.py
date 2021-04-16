from django.db import models


# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=32, verbose_name='�깭洹몃챸')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='�벑濡앹떆媛�')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'fastcampus_tag'  # 테이블명 설정
        verbose_name = '패스트캠퍼스 태그'  # Fcuser 이름 변경
        # 장고는 기본적으로 모델을 보여줄 때 복수형으로 보여주기 때문에 이를 없애주기 위해 아래 코드 구현
        verbose_name_plural = '패스트캠퍼스 태그'
