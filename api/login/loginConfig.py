import json

from api.baseapi import BaseApi


class ForgetPw(BaseApi):

    # 系统页面-登录配置信息的开关状态更改
    def strategy_button(self, sms, email, **kwargs):
        data = {
            'method': 'put',
            'url': self.get_url() + '/v10/config/password/strategy',
            'json': {
                'smsVerificationAfterForgetPassword': sms,
                'emailVerificationAfterForgetPassword': email},
            'headers': {'Authorization': 'Bearer ' + self.get_token()}
        }
        r = self.send(data)
        print('忘记密码-短信和邮箱验证已开启' + json.dumps(r.json()))

    # 获取登录配置信息开关状态
    def strategy_status(self):
        data = {'method': 'get',
                'url': self.get_url() + '/login/config'}
        r = self.send(data)
        return r

    # 忘记密码输入手机或邮箱，获取验证码
    def input_account(self, receiver, type):
        data = {
            'method': 'post',
            'url': self.get_url() + '/login/captcha/gain',
            'json': {'receiver': receiver, 'type': type},
            'headers': {'__device__': 'android'}
        }
        r = self.send(data)
        print("账号输入成功")
        return r
