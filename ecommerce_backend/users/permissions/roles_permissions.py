from users.permissions.roles_permission import IsAdminOrReadOnly



class IsAdmin(BasePermission):
    """
    Allows access only to admin/staff users.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_staff


class IsOwner(BasePermission):
    """
    Allows access only to the owner of a given object.
    """

    def has_object_permission(self, request, view, obj):
        return obj == request.user


class IsAdminOrReadOnly(BasePermission):
    """
    Admins get full access.
    Everyone else gets read-only (GET).
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

