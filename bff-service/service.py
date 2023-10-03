from common import Common
from protos import user_pb2


class UserService:
    @staticmethod
    def get_users():
        # call stub
        stub = Common.get_grpc_service_stub()

        # fill data to request
        user_list_request = user_pb2.UserListRequest(search="test", page=2, size=10)

        # call to gRPC service
        users = stub.GetUsers(user_list_request)

        # convert response from gRPC to JSON
        response = Common.response_data_formater(users)

        # convert status code
        response["status_code"] = Common.convert_status_code(
            response.get("status_code")
        )

        return response

    @staticmethod
    def get_user():
        # call stub
        stub = Common.get_grpc_service_stub()

        # fill data to request
        user_param_request = user_pb2.UserParamRequest(id=1)

        # call to gRPC service
        user = stub.GetUser(user_param_request)

        # convert response from gRPC to JSON
        response = Common.response_data_formater(user)

        # convert status code
        response["status_code"] = Common.convert_status_code(
            response.get("status_code")
        )

        return response
