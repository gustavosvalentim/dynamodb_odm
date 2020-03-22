import setuptools


with open('README.txt') as _f:
    long_description = _f.read()

with open('requirements.txt') as _f:
    requirements = _f.readlines()

setuptools.setup(
    name='dynamodb-odm',
    version='0.1',
    author='Gustavo Valentim',
    author_email='gustavosvalentim1@gmail.com',
    description='ODM library to manage DynamoDB operations.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=requirements,
    python_requires='>=3.6',
    packages=setuptools.find_packages('dynamodb_odm', 'dynamodb_odm.*')
)