Django RBAC Permissions 
=======================

.. contents:: Table of Contents
   :depth: 3

Introduction
============

Django RBAC Permissions is a Django app designed to provide a comprehensive Role-Based Access Control (RBAC) system. The app allows administrators to manage permissions with granularity, specifying permissions based on URL paths or the Django models, with URL permissions taking precedence. It can be easily integrated with Django's class-based views and viewsets.

Features
========

- Map standard CRUD actions to corresponding HTTP methods for consistency.
- Support both URL path-based and model content type-based permissions.
- Prioritize URL-based permissions over model permissions.
- Check user roles and permissions with customizable permission checks.
- Easy to plug into almost any Django Rest Framework (DRF) view with minimal setup.

Requirements
============

- Django >= 2.2
- Django Rest Framework >= 3.11
- Python >= 3.6

Installation
============

To install Django RBAC Permissions within your Django project, follow these steps:

#. Install this repository.

   .. code-block:: bash

       pip install RBAC-service

#. Add the `permissions`, `roles`, and `users` applications to your `INSTALLED_APPS` setting in your Django settings file:

   .. code-block:: python

       INSTALLED_APPS = [
           # ... other installed applications ...

           'rbac_service',
       ]

#. Run the following commands to create the permissions required tables:

   .. code-block:: bash

       python manage.py makemigrations
       python manage.py migrate

Usage
=====

After installing the Django RBAC Permissions app, you can add role-based access control to your views as follows:

#. For views:

   .. code-block:: python

       from rbac_service.permission_classes import RoleBasedPermission

       class MySecureView(APIView):
           permission_classes = (RoleBasedPermission,)
           permission_queryset = MyModel.objects.all() #Your used model in this view
           # Your view code here

#. For viewsets:

   .. code-block:: python

       class MyModelViewSet(viewsets.ModelViewSet):
           permission_classes = (RoleBasedPermission,)
           permission_queryset = MyModel.objects.all() #Your used model in this view
           # Your viewset code here

Configure the permissions for your roles in the Django admin interface, where you can assign URL or model-based permissions to each role.

Contributing
============

Contributions are welcome, and they are greatly appreciated! Every little bit helps, and a credit will always be given.

You can contribute in many ways:

#. Report Bugs
#. Fix Bugs
#. Add Documentation
#. Suggest Features

For details on how to contribute, please check out the CONTRIBUTING.rst file in the repository.

License
=======

Django RBAC Permissions is licensed under the MIT License - see the LICENSE.rst file for more details.

Contact
=======

If you have any questions or want to discuss the project further, please open issues on the repository issue tracker.

Acknowledgements
================

- The Django community for their invaluable resources.
- The developers and maintainers who work on Django and Django Rest Framework.

