from setuptools import setup

dependencies = ['docopt', 'pyyaml', 'inflection']

setup(

    name='Wow',
    version='1.0.0',
    description='Package manager',
    author='Timothee Guerin',
    author_email='timothee Guerin',
    install_requires=dependencies,
    packages=[
        'wow'
    ],
    entry_points={
        'console_scripts': [
            'wow=wow:main'
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 2.6'
    ]
)