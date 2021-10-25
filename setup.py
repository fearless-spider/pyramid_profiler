from setuptools import setup


docs_extras = [
    'Sphinx',
    'docutils',
    'repoze.sphinx.autointerface',
]

tests_require = [
    "pytest",
    "simplejson",
    "sqlalchemy"
]

install_requires = [
    'pyramid',
    'simplejson'
]

setup(
    name='pyramid_profiler',
    version='1.0',
    packages=['pyramid_profiler'],
    url='',
    license=open('LICENSE').read(),
    author='Przemyslaw Pająk',
    author_email='office@fearlessspider.com',
    description='API endpoint profiler for Pyramid framework',
    long_description=open('README.md').read(),
    keywords=[
        'profiler', 'pyramid', 'performance', 'optimization'
    ],
    package_data={
        'pyramid_profiler': [
            'storage/*',
            'static/dist/fonts/*',
            'static/dist/css/*',
            'static/dist/js/*',
            'static/dist/images/*',
            'static/dist/js/*'
            'static/dist/*',
            'static/dist/index.html',
            ]
        },
    test_suite="pyramid_profiler",
    zip_safe=False,
    platforms='any',
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        'docs': docs_extras,
    },
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
        'Framework :: Pyramid',
    ]
)
