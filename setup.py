# coding:utf-8

from setuptools import setup, find_packages

setup(
    name = 'qingcloud-cli',
    version = '0.5',
    description = 'Command Line Interface for QingCloud.',
    long_description = open('README.rst', 'rb').read().decode('utf-8'),
    author = 'Yunify Team',
    author_email = 'simon@yunify.com',
    url = 'https://docs.qingcloud.com/cli/',
    scripts=['bin/qingcloud', ],
    packages = find_packages('.'),
    package_dir = {'qingcloud-cli': 'qingcloud_cli'},
    include_package_data = True,
    install_requires = [
        'argparse>=1.1',
        'PyYAML>=3.1',
    ]
)
