from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='tseopt',
    version='0.1.2',
    packages=find_packages(),
    description=("This library contains code for fetching and processing option data from the Tehran Stock Exchange "
                 "using various public APIs."),
    long_description=long_description,
    long_description_content_type='text/markdown',

    author='Masoud Ghahremani',
    author_email='p.masoud.ghahremani@gmail.com',
    url='https://github.com/masoudghah/TSELiveOptionData',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',
    install_requires=[
        'pandas==2.2.2',
        'requests==2.32.3',
        'fake-useragent==1.5.1',
    ],
    license='MIT',
    keywords='tse options tehran derivative',

)
