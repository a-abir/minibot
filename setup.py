# Run the following command to install package:
# pip install --user .
from setuptools import setup

def readme():
    try:
      with open('README.rst') as f:
          return f.read()
    except:
      return "Minibot"

setup(name='minilib',
      version='0.21',
      long_description=readme(),
      description='Package for adafruit powered servo bots',
      url='http://github.com/atikul99/minibot',
      author='Abir',
      author_email='atikul10152002@gmail.com',
      license='MIT',
      install_requires=[
          'pygame', 'adafruit-circuitpython-crickit'
      ],
      packages=['minilib'],
      zip_safe=False,
      classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.7',
  ],
)
