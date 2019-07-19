import random

import requests

from demo import config as cfg
def generrate_random_number(length=6):

    value = random.randrange(1, 10 ** length)

    template = '%0{}d'.format(length)

    return template % value


def send_vcode(phone_num):
    '''发送验证码'''
    # 生成一个验证码
    vcode = generrate_random_number()

    # 方便调试
    print(vcode)

    params = cfg.YZX_PARAMS.copy()

    params['param'] = '短信验证接口测试 @.@'

    params['mobile'] = phone_num

    # 调用第三方平台接口，发送验证码
    resp = requests.post(cfg.YZX_API, json=params)
    r = resp.json()
    print(resp.status_code, r.get('msg'))
    if resp.status_code == 200:
        result = resp.json()
        if result.get('msg') == 'OK':
            return True
    return False