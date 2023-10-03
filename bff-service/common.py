import json
import os

import grpc
from google.protobuf import json_format
from protos import user_pb2_grpc

from dotenv import load_dotenv

load_dotenv()

GRPC_SERVICE_URL = os.environ.get("GRPC_SERVICE_URL")
USE_SSL = os.environ.get("USE_SSL")


class Common:
    @staticmethod
    def get_grpc_service_stub():
        # sometime when you deploy this on server, it gonna throw error
        # "failed to connect to all addresses"
        # that is because SSL are being used
        # to fix that, we need to call secure_channel() as follow
        # by enable USE_SSL = 1 in .env
        # otherwise, we can do as normal by using insecure_channel()
        # https://github.com/grpc/grpc/issues/28323
        if USE_SSL == "1":
            channel = grpc.secure_channel(
                f"{GRPC_SERVICE_URL}",
                grpc.ssl_channel_credentials(),
                options=(("grpc.enable_http_proxy", 0),),
            )
        else:
            channel = grpc.insecure_channel(f"{GRPC_SERVICE_URL}")

        # call stub
        stub = user_pb2_grpc.UserStub(channel)

        return stub

    @staticmethod
    def convert_status_code(status_code):
        """
        convert gRPC status code to RestAPI status code
        """
        res_status_code = 200
        dict_status_code = {
            "0": 200,
            "1": 499,
            "2": 500,
            "3": 400,
            "4": 504,
            "5": 404,
            "6": 409,
            "7": 403,
            "8": 429,
            "9": 400,
            "10": 409,
            "11": 400,
            "12": 501,
            "13": 500,
            "14": 503,
            "15": 500,
            "16": 401,
        }
        if status_code in dict_status_code.keys():
            res_status_code = dict_status_code[status_code]

        return res_status_code

    @staticmethod
    def response_data_formater(response):
        """
        format rRPC to JSON
        """
        if type(response) is not dict:
            response_json = json_format.MessageToJson(response)
            response_data = json.loads(response_json)
            return response_data

        return response
