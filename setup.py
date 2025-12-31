from setuptools import find_packages,setup

HYPHEN_DOT = "-e ."
def get_packages(file):
    """
    This function return list of necessary packages

    """
    requirements = []
    with open(file) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPHEN_DOT in requirements:
            requirements.remove(HYPHEN_DOT)

    return requirements

        
setup(
    name = "DATA_QUALITY_AND_ANOMALY_DETECTION_SYSTEM",
    version= "1.0",
    author = "Kirti Verma",
    author_email= "kv.edu14@gmail.com",
    packages=find_packages(),
    # install_requires = get_packages('requirements.txt'),
    # install_requires = ['pandas'],

)