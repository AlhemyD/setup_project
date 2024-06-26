from setuptools import setup, find_packages

setup(
   name='setup_test_add',
   version='1.0',
   description='Тестовая функция сложения add для изучения setup.',
   license='Apache-2.0 license',
   author='Tetsushiro Yuji',
   author_email='tetsushiroyuji@gmail.com',
   url='https://github.com/AlhemyD/setup_project.git',
   packages=find_packages(),
   install_requires=['pytest','numpy'],
   extras_require={
        'test': [
            'pytest'
        ],
   },
   python_requires='>=0',
)
