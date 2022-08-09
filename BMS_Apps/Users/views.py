from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import UserBMS, UserRole, UserVisitorDetail, UserStaffDetail
from .serializers import UserSerializer, VisitorProfileSerializer, StaffProfileSerializer, RoleSerializers
import contextlib
from django.http import Http404

# ******************************************************************************************************************
# *******************************************User API***************************************************************
# ******************************************************************************************************************

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API Start
# This API is used for any type of user login.
# type:Web API
# form-data,body
# request key:email,password


class UserLogin(APIView):
    def post(self, request):
        try:
            user_email = request.POST['email']
            user_password = request.POST['password']
            if not (user_status := UserBMS.objects.filter(user_email=user_email, password=user_password).exists()):
                return Response({
                    "data": "false",
                    "status_code": "401",
                    "message": "User not found please check your email and password"
                }, status=status.HTTP_401_UNAUTHORIZED)
            user_data = UserBMS.objects.get(
                user_email=user_email, password=user_password)
            user_serializer = UserSerializer(user_data)
            if user_serializer.data['user_type_name'] == 'Visitors':
                profile_data = UserVisitorDetail.objects.filter(
                    user__id=user_serializer.data['id'])
                profile_serializer = None if len(
                    profile_data) == 0 else VisitorProfileSerializer(profile_data, many=True)

            elif user_serializer.data['user_type_name'] in ['Admin', 'Employee']:
                profile_data = UserStaffDetail.objects.filter(
                    user__id=user_serializer.data['id'])
                profile_serializer = None if len(
                    profile_data) == 0 else StaffProfileSerializer(profile_data, many=True)
            serializer_data = user_serializer.data
            if profile_serializer != None:
                serializer_data.update(
                    {"profile_details": profile_serializer.data})
            else:
                serializer_data.update({"profile_details": []})
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Login Successfully",
                "response": [serializer_data]
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API Start
# This API is used for any type of user add and get list.
# type:Web API
# form-data,raw
# Add ::>> request raw:{'user_type': 1, 'role': 1, 'user_email': 'demo@gmail.com', 'password': '12345678', 'status': False}


class UserAddAndList(APIView):
    def get(self, request):
        try:
            user_data = UserBMS.objects.all()
            all_users = []
            for u in user_data:
                user_serializer = UserSerializer(u)
                if user_serializer.data['user_type_name'] == 'Visitors':
                    profile_data = UserVisitorDetail.objects.filter(
                        user__id=user_serializer.data['id'])
                    profile_serializer = None if len(
                        profile_data) == 0 else VisitorProfileSerializer(profile_data, many=True)

                elif user_serializer.data['user_type_name'] in ['Admin', 'Employee']:
                    profile_data = UserStaffDetail.objects.filter(
                        user__id=user_serializer.data['id'])
                    profile_serializer = None if len(
                        profile_data) == 0 else StaffProfileSerializer(profile_data, many=True)
                serializer_data = user_serializer.data
                if profile_serializer != None:
                    serializer_data.update(
                        {"profile_details": profile_serializer.data})
                else:
                    serializer_data.update({"profile_details": []})
                all_users.append(serializer_data)
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Users List",
                "response": all_users
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        try:
            if email_status := UserBMS.objects.filter(user_email=request.data['user_email']).exists():
                return Response({
                    "data": "false",
                    "status_code": "409",
                    "message": "Email id already exists"
                }, status=status.HTTP_409_CONFLICT)

            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                with contextlib.suppress(Exception):
                    serializer.save()
                    return Response({
                        "data": "true",
                        "status_code": "200",
                        "message": "User account created successfully"
                    }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "data": "false",
                    "status_code": "400",
                    "message": "Invalid data"
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API Start
# This API is used for any type of user update and delete.
# type:Web API
# form-data,raw
# Update ::>> request raw:{"user_type":1,"role":1,"user_email":"mineshpatel@gmail.com","password":"12345678","status":false}


class UserUpdateDeleteDetails(APIView):
    def get_object(self, pk):
        try:
            return UserBMS.objects.get(id=pk)
        except UserBMS.DoesNotExist as e:
            raise Http404 from e

    def get(self, request, pk, format=None):
        user_data = self.get_object(pk)
        try:
            user_serializer = UserSerializer(user_data)
            if user_serializer.data['user_type_name'] == 'Visitors':
                profile_data = UserVisitorDetail.objects.filter(
                    user__id=user_serializer.data['id'])
                profile_serializer = None if len(
                    profile_data) == 0 else VisitorProfileSerializer(profile_data, many=True)

            elif user_serializer.data['user_type_name'] in ['Admin', 'Employee']:
                profile_data = UserStaffDetail.objects.filter(
                    user__id=user_serializer.data['id'])
                profile_serializer = None if len(
                    profile_data) == 0 else StaffProfileSerializer(profile_data, many=True)
            serializer_data = user_serializer.data
            if profile_serializer != None:
                serializer_data.update(
                    {"profile_details": profile_serializer.data})
            else:
                serializer_data.update({"profile_details": []})
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "User's details",
                "response": [serializer_data]
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        delete_user = self.get_object(pk)
        try:
            delete_user.delete()
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "User delete successfully"
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        try:
            email_check = UserBMS.objects.filter(
                user_email=request.data['user_email']).exclude(id=pk).exists()
            if email_check == True:
                return Response({
                    "data": "false",
                    "status_code": "409",
                    "message": "Email id already exists"
                }, status=status.HTTP_409_CONFLICT)
            update_user = UserBMS.objects.get(id=pk)
            serializer = UserSerializer(update_user, data=request.data)
            if serializer.is_valid():
                with contextlib.suppress(Exception):
                    serializer.save()
                    return Response({
                                    "data": "true",
                                    "status_code": "200",
                                    "message": "User update successfully"
                                    }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "data": "false",
                    "status_code": "400",
                    "message": "Invalid data"
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API Start
# This API is used for any type of user change password.
# type:Web API
# form-data,raw
# Register ::>> request raw:{"user_id": "2","old_password": "demo123","new_password" :"123demo"}


class UserChangePassword(APIView):
    def post(self, request):
        try:
            user_id = request.data['user_id']
            old_password = request.data['old_password']
            new_password = request.data['new_password']
            check_old_psw = UserBMS.objects.filter(
                id=user_id, password=old_password).exists()
            if check_old_psw != True:
                return Response({"data": "false", "status_code": "401", "message": "Old password does not matched"}, status=status.HTTP_401_UNAUTHORIZED)
            user_data = UserBMS.objects.get(id=user_id)
            user_data.password = new_password
            user_data.save()
            return Response({
                            "data": "true",
                            "status_code": "200",
                            "message": "Password changed successfully"
                            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API Start
# This API is used for any type of user add profile.
# type:Web API
# form-data,raw
# Add Empoyee Profile::>> request raw:{"user":9,"first_name":"Test", "last_name":"Admin","birthdate":"2022-06-30","department":1,"address":"surat","phone_no":"123456789"}
# Add Visitor Profile::>> request raw: { "user":9,"first_name":"Test","last_name":"Admin","address":"surat","phone_no":"123456789"}


class UserAddProfile(APIView):
    def post(self, request):
        try:
            user_id = request.data["user"]
            user_data = UserBMS.objects.get(id=user_id)
            user_type = user_data.user_type.type_name
            if user_type == 'Visitors':
                serializer = VisitorProfileSerializer(data=request.data)
            elif user_type in ['Admin', 'Employee']:
                serializer = StaffProfileSerializer(data=request.data)
            if serializer.is_valid():
                with contextlib.suppress(Exception):
                    serializer.save()
                    return Response({
                        "data": "true",
                        "status_code": "200",
                        "message": "Profile add successfully"
                    }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "data": "false",
                    "status_code": "400",
                    "message": "Invalid data"
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API Start
# This API is used for any type of user update profile.
# type:Web API
# form-data,raw
# Update Empoyee Profile::>> request raw:{"user":9,"first_name":"Test", "last_name":"Admin","birthdate":"2022-06-30","department":1,"address":"surat","phone_no":"123456789"}
# Update Visitor Profile::>> request raw:{"user": 1,"first_name": "demo","last_name": "demo","birthdate": "2022-06-30","department": 1,"address": "surat","phone_no": "1234546789"}


class UserUpdateProfile(APIView):
    def put(self, request, pk, format=None):
        try:
            user_id = request.data["user"]
            update_profile = UserBMS.objects.get(id=user_id)
            user_type = update_profile.user_type.type_name
            if user_type == 'Visitors':
                visitor_data = UserVisitorDetail.objects.get(id=pk)
                serializer = VisitorProfileSerializer(
                    visitor_data, data=request.data)
            elif user_type in ['Admin', 'Employee']:
                staff_data = UserStaffDetail.objects.get(id=pk)
                serializer = StaffProfileSerializer(
                    staff_data, data=request.data)
            if serializer.is_valid():
                with contextlib.suppress(Exception):
                    serializer.save()
                    return Response({
                                    "data": "true",
                                    "status_code": "200",
                                    "message": "Profile update successfully"
                                    }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "data": "false",
                    "status_code": "400",
                    "message": "Invalid data"
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API Start
# This API is used for get active and in-active users.
# type:Web API
# form-data,raw
# request raw:{"user_id": 3,"isActive": false}


class UserActiveInactive(APIView):
    def post(self, request):
        try:
            user_id = request.data['user_id']
            status_user = request.data['isActive']
            update_status = UserBMS.objects.get(id=user_id)
            update_status.status = status_user
            update_status.save()
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Status updated successfully"
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API End


# ******************************************************************************************************************
# *******************************************Manage Roles **********************************************************
# ******************************************************************************************************************

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API Start
# This API is used for add role and get all role list.
# type:Web API
# form-data,raw
# add role: request raw:{"role_name": "Marketing Manager","permission_ids":[2,3]}

class RoleAddAndList(APIView):
    def get(self, request):
        try:
            user_data = UserRole.objects.all()
            serializer = RoleSerializers(user_data, many=True)
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Role list",
                "response": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        try:
            serializer = RoleSerializers(data=request.data)
            if serializer.is_valid():
                with contextlib.suppress(Exception):
                    serializer.save()
                    return Response({
                        "data": "true",
                        "status_code": "200",
                        "message": "User role created successfully"
                    }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "data": "false",
                    "status_code": "400",
                    "message": "Invalid data"
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API Start
# This API is used for update,delete and view role.
# type:Web API
# form-data,raw
# update role::>request raw:{"role_name": "New Marketing Manager","permission_ids":[2,3,6,7]}


class RoleUpdateDeteleDetails(APIView):
    def get_object(self, pk):
        try:
            return UserRole.objects.get(id=pk)
        except UserRole.DoesNotExist as e:
            raise Http404 from e

    def get(self, request, pk, format=None):
        role_data = self.get_object(pk)
        try:
            serializer = RoleSerializers(role_data)
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Role get successfully",
                "response": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        role_data = self.get_object(pk)
        try:
            serializer = RoleSerializers(role_data, data=request.data)
            if serializer.is_valid():
                with contextlib.suppress(Exception):
                    serializer.save()
                    return Response({
                        "data": "true",
                        "status_code": "200",
                        "message": "User role updated successfully"
                    }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "data": "false",
                    "status_code": "400",
                    "message": "Invalid data"
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        role_data = self.get_object(pk)
        try:
            role_data.delete()
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Role deleted successfully"
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API Start
# This API is used for visitor list.
# type:Web API
# form-data,raw
# update status::>request raw:{"user_id":5,"status":true}


class VisitorList(APIView):
    def get(self, request):
        try:
            user_data = UserBMS.objects.filter(user_type__type_name="Visitors")
            all_users = []
            for u in user_data:
                user_serializer = UserSerializer(u)
                profile_data = UserVisitorDetail.objects.filter(
                    user__id=user_serializer.data['id'])
                profile_serializer = None if len(
                    profile_data) == 0 else VisitorProfileSerializer(profile_data, many=True)
                serializer_data = user_serializer.data
                if profile_serializer != None:
                    serializer_data.update(
                        {"profile_details": profile_serializer.data})
                else:
                    serializer_data.update({"profile_details": []})
                all_users.append(serializer_data)
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Visitor List",
                "response": all_users
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request):
        try:
            user_id = request.data["user_id"]
            user_data = UserBMS.objects.get(id=user_id)
            user_data.status = request.data["status"]
            user_data.save()
            return Response({"data": "true", "status_code": "200", "message": "Status update successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API End
