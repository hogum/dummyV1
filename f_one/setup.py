from setuptools import setup

setup(
    name='f_one',
    packages=['f_one'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
    setup_requires=[
        'pytest-runner'
    ],
    tests_require=[
        'pytest',
    ]

)
