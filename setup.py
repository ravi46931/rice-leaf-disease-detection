from setuptools import setup, find_packages

# Read the contents of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="leaf disease",
    version="0.0.1",
    description="This is a project structure of rice leaf disease detection",
    long_description=long_description,
    author="Ravi Kumar",
    author_email="ravikumar46931@gmail.com",
    url="https://github.com/ravi46931/rice-leaf-disease-detection",
    packages=find_packages(),
    install_requires=[  # List your project's dependencies
        "numpy",  # Example: replace with your actual dependencies
        "pandas",
        # Add other dependencies here
    ],
    include_package_data=True,
)


"""Explanation:
name: The name of your project.

version: The current version of your project.

author and author_email: Your name and email address.

description: A short description of your project.

long_description: A detailed description, typically from your README.md.

long_description_content_type: The format of your long description (e.g., text/markdown for Markdown).

url: The URL for your project’s homepage or repository (if available).

packages: Finds all packages included in your project.

classifiers: Metadata about your project, such as supported Python versions and license.

python_requires: Specifies the minimum Python version required.

install_requires: Lists the dependencies required by your project.

entry_points: Defines command-line scripts, if any.

include_package_data: Ensures non-code files listed in MANIFEST.in are included.

Additional Steps:"""
