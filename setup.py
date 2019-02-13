from setuptools import setup

setup(name='validate_email',
      version='2.0',
      download_url='git@github.com:uwbmrb/validate_email.git',
      py_modules=('validate_email',),
      author='Syrus Akbary and Jon Wedell',
      author_email='wedell@bmrb.wisc.edu',
      description='validate_email verifies if an email address is valid and really exists.',
      long_description=open('README.rst').read(),
      keywords='email validation verification mx verify',
      url='http://github.com/uwbmrb/validate_email',
      license='LGPL',
      install_requires=['dnspython'],
      )
