from distutils.core import setup

setup(
    name='dns_compare',
    version='0.0.4',
    author='Joe Miller',
    author_email='joeym@joeym.net',
    scripts=['dns_compare'],
    url='https://github.com/joemiller/dns_compare',
    license='LICENSE',
    description="Test DNS servers",
    long_description=open('README.markdown').read()
)
