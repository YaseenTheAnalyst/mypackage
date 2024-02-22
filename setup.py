from setuptools import setup, find_packages


setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python pachage',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='',
    author='Mahmoud Yaseen',
    author_email='mahmoudyaseen34@gmail.com'

)