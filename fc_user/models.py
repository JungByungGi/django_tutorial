from django.db import models


# Create your models here.

class Fcuser(models.Model):
    # verbose_name : 사용자가 읽기 쉬운 객체의 이름으로 관리자 화면에서 표시
    username = models.CharField(max_length=32, verbose_name='사용자명')
    useremail = models.EmailField(max_length=128, verbose_name='사용자 이메일')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

    # class媛� 臾몄옄�뿴�쓣 諛섑솚�븷 �븣 媛앹껜 諛섑솚
    def __str__(self):
        return self.username

    # 장고 프레임에게 내가 원하는 것을 전달함
    class Meta:
        db_table = 'fastcampus_fcuser'  # �뀒�씠釉붾챸 �꽕�젙
        verbose_name = "�뙣�뒪�듃罹좏띁�뒪 �궗�슜�옄"  # Fcuser �씠由� 蹂�寃�
        # �옣怨좊뒗 湲곕낯�쟻�쑝濡� 紐⑤뜽�쓣 蹂댁뿬以� �븣 蹂듭닔�삎�쑝濡� 蹂댁뿬二쇨린 �븣臾몄뿉 �씠瑜� �뾾�븷二쇨린 �쐞�빐 �븘�옒 肄붾뱶 援ы쁽
        verbose_name_plural = "�뙣�뒪�듃罹좏띁�뒪 �궗�슜�옄"
