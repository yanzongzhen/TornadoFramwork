# _*_coding:utf-8_*_
"""
@ProjectName: CrawlKeeper
@Author:  Javen Yan
@File: controller.py
@Software: PyCharm
@Time :    2020/1/7 下午4:28
"""
from abc import ABC

from web.apps.default.base import BaseRequestHandler
from web.apps.nodecenter.libs.nodes import get_servers, add_node_server, delete_server


class NodesHandler(BaseRequestHandler, ABC):

    async def get(self):
        response = dict()
        uuid = self.get_argument('uuid', None)
        result = await get_servers(self, uuid)
        response['code'] = result['code']
        response['message'] = result['msg']
        if result['status'] and result.get('data'):
            response['data'] = result.get('data')
        return self.write_json(response)

    async def post(self):
        response = dict()
        server_name = self.get_argument('server_name', None)
        server_url = self.get_argument('server_url', None)
        result = await add_node_server(self, server_name, server_url)
        response['code'] = result['code']
        response['message'] = result['msg']

        return self.write_json(response)

    async def delete(self):
        response = dict()
        uuid = self.get_argument('uuid', None)
        result = await delete_server(self, uuid)
        response['code'] = result['code']
        response['message'] = result['msg']
        return self.write_json(response)
