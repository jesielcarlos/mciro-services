import grpc
from .user_pb2 import UserIdRequest
from .user_pb2_grpc import UserServiceStub

class UserGrpcClient:
    def __init__(self, host='localhost', port=50051):
        self.channel = grpc.insecure_channel(f'{host}:{port}')
        self.stub = UserServiceStub(self.channel)

    def get_user_by_id(self, user_id: int):
        request = UserIdRequest(user_id=user_id)
        return self.stub.GetUserById(request)
