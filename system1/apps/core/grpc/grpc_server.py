from concurrent import futures
import grpc
from apps.core.models import Users
import user_pb2_grpc, user_pb2




class UserServiceServicer(user_pb2_grpc.UserServiceServicer):
    def GetUserById(self, request, context):
        try:
            user = Users.objects.get(id=request.user_id)
            return user_pb2.UserResponse(
                user_id=user.id,
                name=user.name,
                email=user.email
            )
        except Users.DoesNotExist:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('User not found')
            return user_pb2.UserResponse()


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServiceServicer_to_server(Users(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
