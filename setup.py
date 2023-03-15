from setuptools import setup, find_packages

PACKAGE_VERSION = "0.1"
MINOR_RELEASE = "0"

setup(
    name="topic_generator",
    version=f"{PACKAGE_VERSION}.{MINOR_RELEASE}",
    packages=find_packages(where="src"),  # include all packages under src
    package_dir={"": "src"},
    include_package_data=True,

    install_requires=[
        "numpy==1.20.0",
        "pandas",
        "bertopic",
        "umap-learn",
        "hdbscan",
        "scikit-learn",
        "torch@http://download.pytorch.org/whl/cpu/torch-1.9.1%2Bcpu-cp38-cp38-linux_x86_64.whl"
        ],

    author="",
    author_email="",
    description="This package contains topic modeling utilities based on BertTopic library",
    classifiers=[
        ""
    ]
)
