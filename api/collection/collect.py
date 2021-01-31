# 1.查看模板，收藏
# -- check收藏成功
# --check常用列表中有该模板
# 2.取消收藏该模板，（从目录打开该模板取消和从收藏列表打开模板取消收藏是否一样）
# --check取消收藏成功，
# --check收藏列表没有该模板
import json

from api.baseapi import BaseApi


class Collection(BaseApi):
    def __init__(self):
        pass

    # 收藏一张模板,先从目录列表中获取该模板id
    def get_id(self):
        data = {"method": "get",
            "url": self.get_url()+"/v10/mobile/entries",
            'headers': {'__device__': 'android',
                        'Authorization': 'Bearer ' + self.get_token()}
        }
        r = self.send(data)
        # print(json.dumps(r.json(),indent=2))
        self.id=r.json()['data'][0]['id']
        return self.id

    # 收藏模板
    def collect(self):
        data={"method": "post",
            "url": self.get_url()+"/v10/favorite/entry/"+self.id,
            'headers': {'__device__': 'android',
                        'Authorization': 'Bearer ' + self.get_token()}
        }

    # 取消收藏模板
    def delete_collection(self):
        pass

    # 进入收藏列表
    def collection_list(self):
        pass


a = Collection()
print(a.get_id())


