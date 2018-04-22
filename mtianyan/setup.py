from setuptools import setup, find_packages

setup(
    name = "mtianyan",
    version = "0.0.6",
    keywords = ("pip", "mtianyan"),
    description = "mtianyan's tool",
    long_description = "mtianyan's tool",
    license = "MIT Licence",

    url = "http://blog.mtianyan.cn",
    author = "mtianyan",
    author_email = "mtianyan@qq.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ["beautifulsoup4", "requests"]
)