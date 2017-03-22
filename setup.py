from setuptools import setup

setup(name='medivia-api',
      version='0.1',
      description='The Medivia API',
      url='https://github.com/Ethaan/medivia-python-api',
      author='Ethaan',
      author_email='ethan.rosanoo@gmail.com',
      license='MIT',
      packages=['medivia-api'],
      requires=['requests', 'bs4'],
      zip_safe=False
      )