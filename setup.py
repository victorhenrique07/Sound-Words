from setuptools import setup

setup(
    name='Sound-Words',
    packages=['flask_app'],
    include_package_data=True,
    install_requires=[
        'flask',
        'python-dotenv',
        'flask-sqlalchemy'
    ],)
