from distutils.core import setup

classifiers = ['Development Status :: 1 - Beta',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: MIT License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 2.6',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: System :: Hardware']

setup(name	= 'Botluz',
version	= '0.1',
author	= 'Yolanda Robla',
author_email	= 'info@ysoft.biz',
description	= 'A wrapper for John Jays 8 led for children',
long_description= 'A wrapper for John Jays 8 led for children',
license	= 'MIT',
keywords	= 'Raspberry Pi Botluz',
url	= 'http://www.ysoft.biz',
classifiers = classifiers,
py_modules	= ['botluz'],
install_requires= ['RPI']
)
