from protos import user_pb2
from protos import user_pb2_grpc

from faker import Faker

fake = Faker()


class UserServicer(user_pb2_grpc.UserServicer):
    def GetUsers(self, request, context):
        records_number = 10

        user_list_response = user_pb2.UserListResponse(
            items=[],
            page=1,
            total=records_number,
            page_size=records_number
        )

        for _ in range(records_number):
            user_list_response.items.append(
                user_pb2.UserResponse(
                    id=fake.random_int(min=1, max=1000),
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    phone=fake.phone_number(),
                    address=fake.address(),
                    created_date=fake.date_time().strftime(
                        "%m/%d/%Y %H:%M:%S"),
                    created_by=fake.name(),
                    updated_date=fake.date_time().strftime(
                        "%m/%d/%Y %H:%M:%S"),
                    updated_by=fake.name()
                )
            )

        return user_list_response

    def GetUser(self, request, context):
        user_response = user_pb2.UserResponse()
        user_response.id = fake.random_int(min=1, max=1000)
        user_response.first_name = fake.first_name()
        user_response.last_name = fake.last_name()
        user_response.phone = fake.phone_number()
        user_response.address = fake.address()
        user_response.created_date = fake.date_time().strftime("%m/%d/%Y %H:%M:%S")
        user_response.created_by = fake.name()
        user_response.updated_date = fake.date_time().strftime("%m/%d/%Y %H:%M:%S")
        user_response.updated_by = fake.name()

        return user_response
