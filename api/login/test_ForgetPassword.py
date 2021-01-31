from api.login.loginConfig import ForgetPw


class TestVerificationForgetPassword:

    def setup_class(self):
        # 先开启忘记密码-短信邮箱验证
        self.verificationForgetPassword = ForgetPw()
        self.verificationForgetPassword.strategy_button('true', 'true')

    def teardown_class(self):
        # 结束时关闭忘记密码-短信邮箱验证
        self.verificationForgetPassword.strategy_button('false', 'false')

    # 确定忘记密码-验证开启
    def test_open_sms(self):
        r = self.verificationForgetPassword.strategy_status()
        # print(json.dumps(r.json(), indent=2))
        print("确定邮箱和短信开启" + str(r.status_code))
        assert r.json()['data']['smsVerificationAfterForgetPassword'] == True
        assert r.json()['data']['emailVerificationAfterForgetPassword'] == True

    # 判断输入的邮箱不存在
    def test_email_not_exit(self):
        r=self.verificationForgetPassword.input_account("se@fanruan.com",'email')
        print("邮箱不存在测试成功" + str(r.status_code))
        assert r.json()['errorCode'] == '22400010'

    # 判断输入的手机不存在
    def test_sms_not_exit(self):
        r=self.verificationForgetPassword.input_account('12343251421','mobile')
        print("手机不存在测试成功" + str(r.status_code))
        assert r.json()['errorCode'] == '22400010'
