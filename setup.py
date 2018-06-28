import os
from setuptools import find_packages, setup


os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-celery-task-broker',
    version='0.3.0',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='A dynamic Django celery task broker',
    url='https://github.com/lifez/django-celery-task-broker',
    author='Prontotools',
    author_email='prontotools@prontomarketing.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=['django_celery_beat>=1.1.1', 'djangorestframework>=3.6.3']
)
