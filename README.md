# Django Role-Based Permissions API

This project implements a powerful and flexible Role-Based Access Control (RBAC) system, providing granular permissions management down to individual URLs or model-based permissions. Designed to integrate seamlessly with Django's class-based views and viewsets, it offers a high level of control to administrators for securing access to API endpoints.


## Features

- Assign permissions based on models or specific URL paths.
- Prioritize URL-based permissions over model permissions for fine-grained access control.
- Easily applicable to API views or viewsets via `permission_classes` and `permission_queryset`.

## Permission Types
Administrators can set permissions within the Django admin panel. There are two ways to set permissions:

1. URL-Based Permissions: URL permissions have higher priority and can override model permissions. They allow you to restrict access to specific endpoints without relying on linked models. To use them, make sure to set up the url_path field when creating permission records.

2. Model-Based Permissions: When more general control is needed, model permissions can be applied. After creating permissions in the admin panel, define permission_classes and permission_queryset with the corresponding ORM class in your views.


## Getting Started

Start by cloning this repository into your Django project and include the required files.

### Admin Interface:


Use the Django admin to configure permissions for specific URL paths or models. To define permissions for a particular view, create an instance of the Permission model with the desired URL or model settings.

### Configuration codes



To enforce permissions in your API views or viewsets, define the `permission_classes` and `permission_queryset`. Here's an example on how to apply permissions in a sample API view and viewset:

**API View Example:**

```python
class UserAPIView(APIView):
    permission_classes = [RoleBasedPermission]
    permission_queryset = User.objects.all()

    def get(self, request):
        # Your view logic

```
**Viewset Example:**

```python
class UserViewSet(viewsets.GenericViewSet):
    permission_classes = [RoleBasedPermission]
    permission_queryset = User.objects.all()
    # Your view logic


    def List(self, request):
        # Your view logic
```