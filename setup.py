from setuptools import setup

setup(name='mauticapi',
      version='0.2',
      description='An API for Mautic',
      url='http://github.com/kleinq/mauticapi',
      author='kleinq',
      author_email='robert@robertwinder.com',
      license='MIT',
      packages=['mauticapi'],
      install_requires=[
          'rauth',
      ],
      zip_safe=False)