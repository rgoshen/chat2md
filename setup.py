from setuptools import setup, find_packages
from pathlib import Path

readme_path = Path(__file__).parent / "README.md"
long_description = readme_path.read_text(encoding="utf-8") if readme_path.exists() else ""

setup(
    name='chat2md',
    version='0.2.1',
    packages=find_packages(),
    install_requires=[
        'tqdm>=4.65.0',
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "flake8>=5.0",
            "autopep8>=2.0",
        ],
    },
    entry_points={
        'console_scripts': [
            'chat2md=chat2md.cli:main'
        ]
    },
    author='Rick Goshen',
    description='CLI tool to convert ChatGPT-style JSON exports into Markdown with timestamps and syntax-highlighted code blocks.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/rgoshen/chat2md',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.13',
)
