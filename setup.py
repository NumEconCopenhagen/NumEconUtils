from setuptools import find_packages, setup

install_requires = [
    'click'
]
setup_requires = ['pytest-runner']
tests_require=['pytest']

setup(
    name='NumEconUtils',
    author='Jakob Jul Elben',
    version='0.1.0',
    packages=find_packages(),
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    entry_points={
        'console_scripts': [
            'NumEconUtils=NumEconUtils.__main__:cli'
        ]
    }
)