from django.shortcuts import render, redirect
from .models import Fcuser
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .forms import LoginForm


def home(request):
    return render(request, 'home.html')


#로그인
def login(request):
    '''
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        res_data = {}
        if not (username and password):
            res_data['error'] = '모든 값을 입력해야 합니다.'
        else:
            fcuser = Fcuser.objects.get(username=username)
            # print(fcuser)
            # print(fcuser.password)
            # print(password)
            # print(check_password(password, fcuser.password))
            if check_password(password, fcuser.password):  #check_password library사용 ->암호화된 비밀번호에 한해서 true값 반환
                #로그인 처리(비밀번호 일치)
                #세션
                #로그인 완료 시 홈으로 이동(redirect)
                request.session['user'] = fcuser.id
                return redirect('/')  # slash만 쓰면 root로 이동 -> 홈 화면으로 이동하기

            else:
                res_data['error'] = '비밀 번호를 틀렸습니다.'

        return render(request, 'login.html', res_data)

    '''
    # form 활용하기
    if request.method == 'POST':
        form = LoginForm(request.POST)
        # is_valid를 통해 FORM 안에 error 정보가 들어 있음.
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        form = LoginForm
    return render(request, 'login.html', {'form': form})



def logout(request):
    if request.session.get('user'):
        del (request.session['user'])
    return redirect('/')


def register(request):
    # 회원가입 로직
    if request.method == 'GET':
        return render(request, 'register.html')
    # 템플릿 폴더를 이미 바라보고 있으므로 경로를 찾을 수 있음.
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        useremail = request.POST.get('useremail', None)
        re_password = request.POST.get('re-password', None)
        res_data = {}
        if not (username and useremail and password and re_password):
            res_data['error'] = '모든 값을 입력해야 합니다.'
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            fcuser = Fcuser(
                username=username,
                useremail=useremail,
                password=make_password(password)  # 비밀번호 암호화
            )
            fcuser.save()

        return render(request, 'register.html', res_data)
