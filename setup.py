"""
Django-Gtranslate
-------------
A Django app to add Googletrans google translation to the template 
with ability to cache translation to external pretty .json file
"""
from setuptools import setup


setup(
    name='Django-Gtranslate',
    version='0.6',
    url='https://github.com/mrf345/django_gtranslate/',
    download_url='https://github.com/mrf345/django_gtranslate/archive/0.6.tar.gz',
    license='MIT',
    author='Mohamed Feddad',
    author_email='mrf345@gmail.com',
    description='Googletrans google translation django app',
    long_description=__doc__,
    packages=['django_gtranslate'],
    include_package_data=True,
    platforms='any',
    install_requires=[
        'django',
        'googletrans'
    ],
    keywords=['django', 'extension', 'google', 'translate', 'googletrans', 'json'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)