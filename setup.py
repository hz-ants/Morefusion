from setuptools import find_packages
from setuptools import setup
import shlex
import subprocess


def git_version():
    cmd = 'git log --format="%h" -n 1'
    return subprocess.check_output(shlex.split(cmd)).decode().strip()


version = git_version()

setup(
    name='objslampp',
    version=version,
    packages=find_packages(),
    install_requires=[],  # see requirements.txt
    author='Kentaro Wada',
    author_email='www.kentaro.wada@gmail.com',
    license='MIT',
    url='https://github.com/wkentaro/objslampp',
    description='Volumetric fusion and CAD alignment for object-level SLAM',
)
