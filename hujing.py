import requests

__doc__ = """
虎鲸跳跃，微信ocr数据接口测试
"""
PATH = 'http://aiapi.aihujing.com/'
# 通话记录
phone_list_url = PATH + 'phone/list'
# 聊天接口
chat_list_url = PATH + 'chat/list'
# 销售创建群
group_list_url = PATH + 'group/list/own'
# 添加好友列表
contact_list_url = PATH + 'contact/list/add'
# 删除好友列表
contact_list_del_url = PATH + 'contact/list/del'
# 规则引擎接口
rule_list_url = PATH + 'rule/engine/list'


def test():
    res = requests.get(chat_list_url, params={'start_time': '2019-02-19 00:00:00',
                                               'appid': 'trrt0122'})
    # res = requests.get(contact_list_url, params={'create_time': '2019-01-20 00:00:00',
    #                                                 'appid': 'trrt0122',
    #                                                  'page': 1})
    print(type(res))
    print(res.text)
    print(res.json())
    # for i in res.json().get('data').get('list'):
    #     print(i)


if __name__ == '__main__':
    test()
