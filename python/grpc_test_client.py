import grpc
import time
import test_pb2
import test_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = test_pb2_grpc.GreeterStub(channel)
    duration = 10
    end = time.time() + duration
    msgs = 0
    data = b'b' * (1 << 20)
    while time.time() < end:
        response = stub.SendData(test_pb2.Request(name=data))
        msgs += 1

    print('Received {} messages in {} second(s).'.format(msgs, duration))


if __name__ == '__main__':
    run()
