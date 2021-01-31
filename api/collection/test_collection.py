import json

from dataAnalysis.api.baseapi import BaseApi


class TestCollection(BaseApi):

    # 收藏一张模板,先从目录列表中获取该模板id
    def test_get_id(self):
        data = {"method": "get",
            "url": self.get_url()+"/v10/mobile/entries",
            'headers': {'__device__': 'android',
                        'Authorization': 'Bearer ' + self.get_token()}
        }
        r = self.send(data)
        print(json.dumps(r.json()))
        # return r
        assert r.status_code==200

    # 收藏模板
    def collect(self):
        pass

    # 取消收藏模板
    def delete_collection(self):
        pass

    # 进入收藏列表
    def collection_list(self):
        pass


# a = Collection()
# print(a.get_id())