try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='Wrapper',
    packages=['wrapper'],
    version='0.1',
    license="GPL",
    description='Random API Wrappers',
    author='Biwin John',
    author_email='biwinjohn@gmail.com',
    url='https://github.com/biwin/wrapper',
    download_url='https://github.com/biwin/wrapper/archive/0.1.tar.gz',
    install_requires=[],
    requires=['requests', 'barcodenumber'],
    keywords=['api', 'python'],
    classifiers=[],
)
