from setuptools import setup, find_packages

setup(
	name='assignment0',
	version='1.0',
	author='Your Name',
	authour_email='your ou email',
	packages=find_packages(exclude=('tests', 'docs')),
	setup_requires=['pytest-runner'],
	tests_require=['pytest']	
)
