# !/usr/bin/python
# -*- coding:utf-8 -*-
import requests
import json


def requestRasabotServer(content):
    """
    访问rasa服务
    :param content: 自然语言文本
    :return:  json格式响应数据
    """
    params = {'message': content}
    botIp = '192.168.100.210'
    botPort = '9900'
    # https://rasa.com/docs/rasa/user-guide/connectors/your-own-website/#rest-channels
    # POST /webhooks/rest/webhook
    rasaUrl = "http://{0}:{1}/webhooks/rest/webhook".format(botIp, botPort)
    Response_post = requests.post(
        rasaUrl,
        data=json.dumps(params),
        headers={'Content-Type': 'application/json'}
    )
    text = Response_post.text
    return text.encode('utf-8').decode('unicode_escape')


if __name__ == '__main__':
    content = input("input:")
    answer = requestRasabotServer(content)
    print(answer)

    while answer:
        content = input("input:")
        answer = requestRasabotServer(content)
        print(answer)
