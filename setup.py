from setuptools import setup, find_packages

setup(
    name='query',
    version='1.0',
    packages=find_packages(exclude=['scripts']),
    url='https://github.com/Ais105/kursach',
    license='MIT',
    author='ais',
    author_email='krissvarcnegger@gmail.com',
    description='not int osq for git',
    install_requires=['gitpython','pygithub','plotly'],
    zip_safe=False,
)
