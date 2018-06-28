import setuptools

if __name__ == "__main__":
    setuptools.setup(
        name='RTP_python_template',
        version="0.3.0",
        description='A starting template for Python programs',
        author='Doaa Altarawy',
        author_email='daltarawy@vt.edu',
        url="https://github.com/doaa-altarawy/RTP_python_template",
        license='BSD-3C',
        packages=setuptools.find_packages(),
        install_requires=[
            'numpy>=1.7',
        ],
        extras_require={
            'docs': [
                'sphinx==1.2.3',  # autodoc was broken in 1.3.1
                'sphinxcontrib-napoleon',
                'sphinx_rtd_theme',
                'numpydoc',
            ],
            'tests': [
                'pytest>=3.0',
                # 'codecov',
                'pytest-cov',
                'pytest-pep8',
            ],
        },

        # tests_require=[
        #     'pytest',
        #     'pytest-cov',
        #     'pytest-pep8',
        # ],

        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Science/Research',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
        ],
        zip_safe=True,
    )
