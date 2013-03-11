from setuptools import setup
import os.path

version = '0.1dev'

long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CREDITS.rst').read(),
    open('CHANGES.rst').read(),
    ])

install_requires = [
    'setuptools',
    'coverage > 3.3.1',
    'pep8',
    'pyflakes',
    ],

tests_require = [
    ]

setup(name='hudsonintegration',
      version=version,
      description="Provides command that runs tests like we want for hudson",
      long_description=long_description,
      # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[],
      keywords=[],
      author='Reinout van Rees',
      author_email='reinout.vanrees@nelen-schuurmans.nl',
      url='',
      license='GPL',
      packages=['hudsonintegration'],
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      tests_require=tests_require,
      extras_require = {'test': tests_require},
      entry_points={
          'console_scripts': [
            'run_tests = hudsonintegration.runner:run_tests',
            'create_reports = hudsonintegration.runner:create_reports',
            'run_jslint = hudsonintegration.runner:run_jslint',
            'jslint = hudsonintegration.jslint:main',
          ]},
      )
