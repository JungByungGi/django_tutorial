from django.db import models


# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=128, verbose_name='�젣紐�')
    contents = models.TextField(verbose_name='�궡�슜')
    # tag(M:N관계) -> 하나의 태그에 여러 글 가능 / 하나의 글에 여러 태그 가능
    tags = models.ManyToManyField('tag.Tag', verbose_name='�깭洹�')
    # on_delete=models.CASCADE : 사용자가 탈퇴 시 그 사용자가 쓴 모든 글을 탈퇴하겠다는 명령 (ForeignKey(1:N) : id로 연결)
    writer = models.ForeignKey('fc_user.Fcuser', on_delete=models.CASCADE, verbose_name='�옉�꽦�옄')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='�벑濡앹떆媛�')

    # class의 객체의 문자열 표현을 리턴(title을 return )
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'fastcampus_board'  # 테이블명 설정
        verbose_name = "패스트캠퍼스 게시글"  # Fcuser 이름 변경
        verbose_name_plural = "패스트캠퍼스 게시글"
