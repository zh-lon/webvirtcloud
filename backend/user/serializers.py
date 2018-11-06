from rest_framework import status
from rest_framework.response import Response
from rest_framework import serializers
from rest_auth.views import LoginView
from rest_auth.registration.views import RegisterView
from allauth.account import app_settings as allauth_settings

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email',)


class SignUpView(serializers.Serializer):
    email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    # def validate_username(self, username):
    #     username = get_adapter().clean_username(username)
    #     return username
    #
    # def validate_email(self, email):
    #     email = get_adapter().clean_email(email)
    #     if allauth_settings.UNIQUE_EMAIL:
    #         if email and email_address_exists(email):
    #             raise serializers.ValidationError(
    #                 _("A user is already registered with this e-mail address."))
    #     return email
    #
    # def validate_password1(self, password):
    #     return get_adapter().clean_password(password)
    #
    # def validate(self, data):
    #     if data['password1'] != data['password2']:
    #         raise serializers.ValidationError(_("The two password fields didn't match."))
    #     return data
    #
    # def custom_signup(self, request, user):
    #     pass
    #
    # def get_cleaned_data(self):
    #     return {
    #         'username': self.validated_data.get('username', ''),
    #         'password1': self.validated_data.get('password1', ''),
    #         'email': self.validated_data.get('email', '')
    #     }

    def save(self, request):
        # adapter = get_adapter()
        # user = adapter.new_user(request)
        # self.cleaned_data = self.get_cleaned_data()
        # adapter.save_user(request, user, self)
        # self.custom_signup(request, user)
        # setup_user_email(request, user, [])
        # return
        return ''

# class SignUpView(RegisterView):
#
#     def get_response_data(self, user):
#         if allauth_settings.EMAIL_VERIFICATION == \
#                 allauth_settings.EmailVerificationMethod.MANDATORY:
#             return {"detail": _("Verification e-mail sent.")}
#         serializer = UserSerializer(user)
#         data = {
#             'user': serializer.data,
#             'session': self.request.session.session_key,
#             'token': self.token
#         }
#         return data


class SignInView(LoginView):

    def get_response(self):
        serializer_class = self.get_response_serializer()
        serializer = UserSerializer(self.user)
        data = {
            'user': serializer.data,
            'session': self.request.session.session_key,
            'token': self.token
        }
        serializer = serializer_class(instance=data,
                                      context={'request': self.request})

        return Response(serializer.data, status=status.HTTP_200_OK)
