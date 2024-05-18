from setuptools import setup, find_packages

setup(
   long_description=open('README.md').read(),
   long_description_content_type='text/markdown',
   name='setup_test_addy',
   version='1.0',
   description='Тестовая функция сложения add для изучения setup.',
   license='Apache-2.0 license',
   author='Tetsushiro Yuji',
   author_email='tetsushiroyuji@gmail.com',
   url='https://github.com/AlhemyD/setup_project.git',
   packages=find_packages(),
   install_requires=['pytest','numpy','matplotlib'],
   extras_require={
        'test': [
            'pytest'
        ],
   },
   python_requires='>=0',
)
