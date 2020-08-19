from setuptools import setup

setup(
    name='dns_compare',
    version='0.0.3',
    author='Jean-Francois Chevrette',
    author_email='jfchevrette@gmail.com',
    scripts=['dns_compare'],
    url='https://github.com/jfchevrette/dns_compare',
    license='LICENSE',
    description="Test DNS servers",
    long_description=open('README.markdown').read(),
    python_requires='>=3.6',
    install_requires=[
        'dnspython ~= 2.0',
    ]
)
