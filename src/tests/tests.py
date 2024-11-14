# import logging
# from django.db.models import F
# from user.models import CustomUser, Role, RoleForUser, Profile

# logger = logging.getLogger("cons")

# class TestCases():

#     def tests_register_user(self, api_client):
#         data = {
#             "username": "testuser",
#             "email": "testuser@example.com",
#             "password": "testpass123",
#             "password2": "testpass123"
#         }
#         response: Response = api_client.post("/api/v1/users/register/", data=data, format='json') #type: ignore
#         assert response.status_code, 201

#         data["password"] = "rerssdsds"
#         response: Response = api_client.post("/api/v1/users/register/", data=data, format='json') #type: ignore
#         assert response.status_code, 400

#         assert Profile.objects.get(user_id=1).pk, 1
#         assert len(RoleForUser.objects.filter(user_id=1)), 1

#     def tests_delete_user(self, api_client, create_user):

#         response: Response = api_client.delete(f"/api/v1/users/{1}", format='json')
#         for i in CustomUser.objects.all():
#             logger.info(i)
#         for i in RoleForUser.objects.all():
#             logger.info(i.user)
#         for i in Profile.objects.all():
#             logger.info(i.user)
#         assert response.status_code, 204

#     def tests_get_users(self, api_client):
#         response: Response = api_client.get("/api/v1/users/", format="json") #type: ignore
#         logger.info(response.json())
