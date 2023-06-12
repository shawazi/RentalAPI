from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            return True

        allowed = bool(request.user and request.user.is_staff)
        return allowed

class IsCustomer(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated
        return False
    
    def has_object_permission(self, request, view, obj):
        print(request.user.id)
        print(obj.customer_id)
        
        if request.user.is_staff:
            return True
        return obj.customer_id == request.user.id