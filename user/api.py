from django.http import JsonResponse

from user.logics import send_vcode


def get_vcode(request):
    # 获取验证码接口
    phone_num = request.GET.get('phone_num')
    is_success = send_vcode(phone_num)
    return JsonResponse({'code': 0, 'data':is_success})


def submit_vcode(request):
    # 提交验证码，进行登录或者注册
    return JsonResponse()
