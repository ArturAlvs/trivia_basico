from rest_framework.permissions import BasePermission

class IsAllowedToWriteIfOwnAndReadIfLogged(BasePermission):

	def has_object_permission(self, request, view, obj):

		SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']


		if (request.method in SAFE_METHODS or (obj.user_criador == request.user) ):
			return True

		return False

	def has_permission(self, request, view):

		if (request.user and request.user.is_authenticated ):
			return True

		return False
