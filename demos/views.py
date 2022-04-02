from unittest import result
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def calculator(request):
    # return HttpResponse("계산기 기능 구현 시작입니다. 1111") -> HttpResponse는 template을 사용하지 않아도 view.py로만 가능하다. 근데 실질적으로는 render만 기억해서 쓰면 된다.
    # 디버깅: 1. print를 활용한 디버깅 2. 디버그 모드를  활용한 디버깅
    print(f'request = {request}')
    print(f'request type = {type(request)}')
    print(f'request.__dict__ = {request.__dict__}')

    # 1. 데이터 확인
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    operators = request.GET.get('operators')

    # 2. 계산
    if operators == '+':
        result = int(num1) + int(num2)
    elif operators == '-':
        result = int(num1) - int(num2)
    elif operators == '*':
        result = int(num1) * int(num2)
    elif operators == '/':
        result = int(num1) / int(num2)
    else:
        result = 0

    # 3. 응답
    return render(request, 'calculator.html', {'result': result})


def lotto(request):
    # 2. 계산
    import random
    lotto_nums = random.sample(range(1, 45), 6)

    # 3. 응답
    return render(request, 'lotto.html', {'lotto_nums': lotto_nums})
