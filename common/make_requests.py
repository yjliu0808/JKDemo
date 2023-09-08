"""
=================================================
Author : Athena
Time : 2023/8/20 15:34 
=================================================
"""
# title	method	url	request_data	expect_data
# 登录成功	post	http://101.35.51.221:8099/admin/login	{"username":"test","password":"123456"}	{"code":200,"message":"操作成功"}

import requests

def send_http_request(url, method,**kwargs) -> requests.Request:
       #

        #把方法名小写化，防止误传
        method = method.lower()
        #获取对应方法：返回对应的方法

        return getattr(requests,method)(url=url,**kwargs)

        # if method == 'get':
        #     response = requests.get(url=url,params=params , json=json,headers=headers,  data=data, files=files)
        # elif method == 'post':
        #     headers={'Content-Type':'application/json'}
        #     response = requests.post(url=url, headers=headers, json=json, data=data, files=files)
        # elif method == 'patch':
        #     headers={'Content-Type':'application/json'}
        #     response = requests.patch(url=url, headers=headers, json=json, data=data, files=files)
        # elif method == 'delete':
        #     headers = {'Content-Type': 'application/json'}
        #     response = requests.delete(url=url, headers=headers, json=json, data=data, files=files)
        # return response

# if __name__ == '__main__':
#     case = {
#         'id': 1,
#         'title': "登录",
#         'method': 'post',
#         'url': 'http://101.35.51.221:8099/admin/login',
#         'request_data': {"username": "test", "password": "123456"},
#         'expect_data': {"code": 200, "message": "操作成功"}
#     }
#
# response = send_http_request(url=case['url'], method=case['method'],json=case['request_data'])
# print(response.text)
# print(response.status_code)
