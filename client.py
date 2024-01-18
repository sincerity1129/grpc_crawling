from __future__ import print_function

import logging

import grpc
from pb2file import crawler_pb2
from pb2file import crawler_pb2_grpc
from config.cfg import basic_cfg


def run():
    conn_ip = f'{basic_cfg["host"]}:{basic_cfg["port"]}'
    with grpc.insecure_channel(conn_ip) as channel:
        stub = crawler_pb2_grpc.crawlerProcessStub(channel)
        response = stub.crawler(crawler_pb2.CRAWLERRequest(url="start"))
    print("Greeter client received: " + response.data)


if __name__ == "__main__":
    logging.basicConfig()
    run()
