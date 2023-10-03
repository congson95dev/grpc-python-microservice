from concurrent import futures

import grpc

from protos import user_pb2_grpc

from services import UserServicer


def run():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServicer_to_server(UserServicer(), server)

    # url: 127.0.0.1:50051
    server.add_insecure_port("0.0.0.0:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    run()
