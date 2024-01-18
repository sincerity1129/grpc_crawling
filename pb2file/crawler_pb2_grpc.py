# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from pb2file import crawler_pb2 as crawler__pb2


class crawlerProcessStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.crawler = channel.unary_unary(
                '/crawlerProcess.crawlerProcess/crawler',
                request_serializer=crawler__pb2.CRAWLERRequest.SerializeToString,
                response_deserializer=crawler__pb2.CRAWLERReply.FromString,
                )
        self.crawlerStreamReply = channel.unary_stream(
                '/crawlerProcess.crawlerProcess/crawlerStreamReply',
                request_serializer=crawler__pb2.CRAWLERRequest.SerializeToString,
                response_deserializer=crawler__pb2.CRAWLERReply.FromString,
                )


class crawlerProcessServicer(object):
    """Missing associated documentation comment in .proto file."""

    def crawler(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def crawlerStreamReply(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_crawlerProcessServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'crawler': grpc.unary_unary_rpc_method_handler(
                    servicer.crawler,
                    request_deserializer=crawler__pb2.CRAWLERRequest.FromString,
                    response_serializer=crawler__pb2.CRAWLERReply.SerializeToString,
            ),
            'crawlerStreamReply': grpc.unary_stream_rpc_method_handler(
                    servicer.crawlerStreamReply,
                    request_deserializer=crawler__pb2.CRAWLERRequest.FromString,
                    response_serializer=crawler__pb2.CRAWLERReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'crawlerProcess.crawlerProcess', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class crawlerProcess(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def crawler(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/crawlerProcess.crawlerProcess/crawler',
            crawler__pb2.CRAWLERRequest.SerializeToString,
            crawler__pb2.CRAWLERReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def crawlerStreamReply(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/crawlerProcess.crawlerProcess/crawlerStreamReply',
            crawler__pb2.CRAWLERRequest.SerializeToString,
            crawler__pb2.CRAWLERReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
