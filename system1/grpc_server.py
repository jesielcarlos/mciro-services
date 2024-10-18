from concurrent import futures
import grpc
from users.grpc import user_pb2_grpc, user_pb2
from users.models import User



class UserServiceServicer(user_pb2_grpc.UserServiceServicer):
    def GetUserById(self, request, context):
        try:
            user = User.objects.get(id=request.user_id)
            return user_pb2.UserResponse(
                user_id=user.id,
                name=user.name,
                email=user.email
            )
        except User.DoesNotExist:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('User not found')
            return user_pb2.UserResponse()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServiceServicer_to_server(UserServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
