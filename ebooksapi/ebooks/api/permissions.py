from rest_framework import permissions

class IsAdminUserOrReadOnly(permissions.IsAdminUser):
    """ solo gli utenti admin possono creare e aggiornare istanze di ebook """

    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        return request.method in permissions.SAFE_METHODS or is_admin


class IsReviewAuthorOrReadOnly(permissions.BasePermission):
    """ update e delete concessi solo agli autori della review """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.review_author == request.user
