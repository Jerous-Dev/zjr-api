from setuptools import setup, find_packages
from pathlib import Path

VERSION = '1.0.0'
DESCRIPTION = 'zjr-api: Zalo API for Python'
this_directory = Path(__file__).parent
LONG_DESCRIPTION = (this_directory / "README.md").read_text()

# Setting up
setup(
    name="zjr-api",
    version=VERSION,
    tranformer="Lâm Minh Phú (Jerous)",
    tranformer_email=["zalochatbot@gmail.com", "zbllf2lollpll@gmail.com"],
    transformer_phone_number="0816262451",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests', 'aiohttp', 'aenum', 'attr', 'pycryptodome', 'datetime', 'munch', 'websockets'],
    keywords=['python', 'zalo', 'api', 'zalo api', 'zalo chat', 'requests'],
    classifiers=[
		"Development Status :: 3 - Alpha",
		"Intended Audience :: Developers",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
		"Natural Language :: English",
		"Programming Language :: Python",
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: Implementation :: CPython",
		"Programming Language :: Python :: Implementation :: PyPy",
		"Topic :: Communications :: Chat",
		"Topic :: Internet :: WWW/HTTP",
		"Topic :: Internet :: WWW/HTTP :: Dynamic Content",
		"Topic :: Software Development :: Libraries",
		"Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
