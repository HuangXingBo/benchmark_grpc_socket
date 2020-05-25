from concurrent import futures
import time
import grpc
import test_pb2
import test_pb2_grpc


class TestServer(test_pb2_grpc.GreeterServicer):

    def SendData(self, request, context):
        return test_pb2.Reply(message="Hello there!".encode('utf-8'))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    test_pb2_grpc.add_GreeterServicer_to_server(TestServer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    try:
        while True:
            time.sleep(60 * 60 * 24)  # one day in seconds
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
