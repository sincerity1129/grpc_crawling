from concurrent import futures

import grpc
from pb2file import crawler_pb2
from pb2file import crawler_pb2_grpc
from config.cfg import basic_cfg


class CrawlerProcess(crawler_pb2_grpc.crawlerProcessServicer):    
    def crawler(self, request, context):
        return crawler_pb2.CRAWLERReply(data="Hello, %s!" % request.url)


def serve(logger):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=basic_cfg['max_workers']))
    crawler_pb2_grpc.add_crawlerProcessServicer_to_server(CrawlerProcess(), server)
    server.add_insecure_port("[::]:" + basic_cfg['port'])
    server.start()
    print('Service API Start')
    logger.info("Server started, listening on " + basic_cfg['port'])
    server.wait_for_termination()
    