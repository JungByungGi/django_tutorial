from django.shortcuts import render, redirect
from django.http import Http404
from django.core.paginator import Paginator
from .models import Board
from .forms import BoardForm
from fc_user.forms import Fcuser
from tag.models import Tag


# Create your views here.
def board_list(request):
    # id 역순으로 가지고 옴
    all_boards = Board.objects.all().order_by('-id')
    page = int(request.GET.get('p', 1))
    paginator = Paginator(all_boards, 3)

    boards = paginator.get_page(page)
    return render(request, 'board_list.html', {'boards': boards})


def board_write(request):
    # 로그인하지 않은 사용자가 글을 작성할 수 없게 로그아웃 상황 시 board/write 주소로 가면 로그인을 먼저 할 수 있게끔 구현
    if not request.session.get('user'):
        return redirect('/fcuser/login')

    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            # 사용자는 세션에 존재
            user_id = request.session.get('user')
            fcuser = Fcuser.objects.get(pk=user_id)
            tags = form.cleaned_data['tags'].split(',')

            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = fcuser

            board.save()

            for tag in tags:
                if not tag:
                    continue
                # 값을 가지고 오거나 없으면 생성
                _tag, _ = Tag.objects.get_or_create(name=tag)
                board.tags.add(_tag)

            return redirect('/board/list/')

    else:
        form = BoardForm()

    return render(request, 'board_write.html', {'form': form})


# 몇 번째 게시글인지 알아야 하므로 pk를 파라미터로 추가
def board_detail(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다.')
    return render(request, 'board_detail.html', {'board': board})
