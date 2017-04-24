try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='Wrapper',
    packages=['wrapper'],
    version='1.0.0',
    license="GPL",
    description='A wrapper around several APIs.',
    author='Biwin John',
    author_email='biwinjohn@gmail.com',
    url='https://github.com/biwin/wrapper',
    download_url='https://github.com/biwin/wrapper/archive/0.1.tar.gz',
    install_requires=[],
    requires=['requests', 'barcodenumber'],
    keywords=['api', 'python'],
    classifiers=[],
)
