import requests
from django.conf import settings


def get_wb_access_token(code):
    '''获取微博 access_token'''
    args = settings.WB_ACCESS_TOKEN_ARGS.copy()
    args['code'] = code
    response = requests.post(settings.WB_ACCESS_TOKEN_API, data=args)
    if response.status_code == 200:
        return response.json()
    else:
        return {'error': 'Weibo server error'}


def get_wb_user_show(access_token, uid):
    '''获取微博个人信息'''
    args = settings.WB_USER_SHOW_ARGS.copy()
    args['access_token'] = access_token
    args['uid'] = uid
    response = requests.get(settings.WB_USER_SHOW_API, params=args)
    if response.status_code == 200:
        return response.json()
    else:
        return {'error': 'Weibo server error'}
