from setuptools import setup, find_packages

setup(
    name="RBAC_service",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'Django',
    ],
    include_package_data=True,
    license="MIT",
    description="Django Role-Based Permission App",
    long_description=open("README.rst").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/shirani98/rbac_service",
    author="Mahdi Shirani",
    author_email="Shirani9882@gmail.com",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)

