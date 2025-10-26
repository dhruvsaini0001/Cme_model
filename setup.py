## from distutils.core import setup  (old way)
from setuptools import find_packages, setup # (new way)

HYPEN_E_DOT = '-e .'


def get_requirements(file_path: str) -> list[str]:
    """Return a list of requirement strings from a requirements file.

    - Strips whitespace
    - Ignores empty lines and comments
    - Ignores editable/local installs (lines starting with '-e' or 'git+')
    """
    
    requirements: list[str] = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            req = line.strip()
            if not req:
                continue
            if req.startswith("#"):
                continue
            if req.startswith("-e") or req.startswith("git+"):
                continue
            requirements.append(req)

    return requirements

setup(
    name='CME_DETECTION',
    version='0.0.1',
    author='DHRUV SAINI',
    author_email='dhruvsaini2209@gmail.com',
    # use top-level package discovery instead of src/ layout
    packages=find_packages(),
    # install_requires=['pandas','numpy','seaborn','matplotlib','scikit-learn','flask','xgboost','lightgbm','catboost'], 
    install_requires=get_requirements('requirements.txt')
)




#Normal install → Making a photocopy of your book. Changing the original book doesn’t change the photocopy.

#Editable install (-e .) → Putting a bookmark to the original book. Any edits you make to the book are seen immediately when you read it.