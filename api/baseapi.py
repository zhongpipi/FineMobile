import pytest
import requests
import yaml


class BaseApi:
    def __init__(self):
        with open("baseData.yml", encoding="utf-8") as f:
            self.data=yaml.load(f,Loader=yaml.FullLoader)

    # 通过登录获取token
    @pytest.mark.parametrize('user,pwd',yaml.safe_load(open("baseData.yml")))
    def get_token(self,user,pwd):
        data = {
            "method": "post",
            'url': self.get_url()+'/login',
            'json': {
                'encrypted': 'true',
                'password': user,
                'username': pwd,
                'validity': -1
            }}
        r=self.send(data)
        # print(r.json()['data']['accessToken'])
        return r.json()['data']['accessToken']

    # 封装请求
    def send(self, kwargs):
        r = requests.request(**kwargs)
        # print(json.dumps(r.json(), indent=2))
        return r

    # 从baseData.yaml获取平台地址
    def get_url(self):
        return self.data['url']


print(BaseApi().get_url())