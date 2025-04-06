from setuptools import setup, find_packages

setup(
    name='chat2md',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'chat2md=chat2md.cli:main'
        ]
    },
    author='Rick Goshen',
    description='CLI tool to convert ChatGPT-style JSON exports into Markdown with timestamps and syntax-highlighted code blocks.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/chat2md',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License'
    ],
    python_requires='>=3.7',
)
