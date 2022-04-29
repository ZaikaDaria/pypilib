# Publishing own package to PyPi
## Step 1: Create the __init__.py file
Create a file named __init__.py and save it into the same folder your code is. This file tells Python that the folder contains a Python package. The code inside the __init__.py file gets run whenever you import a package inside a Python program. In this case, my __init__.py file is importing GuessMyNumber class from the numberGuesserGame module.
## Step 2: Create the setup.py file
Go up one level in the directory and create the setup.py file.
This important file contains information about the package. Every time you run the command pip, it will automatically look for the setup.py file.
It basically consists of a call to the setup function, which receives arguments to specify details of how the project is defined, for example, name, author, version, description, etc.
## Step 3: Install your package locally
After you completed steps 1 and 2, everything is ready to install your Python package locally. First, open a terminal and go to the folder containing your package and type the command below. The dot indicates to look for a setup.py file in the current folder and install the package in there.
```
pip install .
```
## Step 4: Create the License and README files
Come back to the directory containing your package and create two more files:<br>

<em><strong>License.txt</strong></em> will tell users the terms and conditions under which they can use your package. I copied and pasted into my file the MIT license<br>
<em><strong>README.md</strong></em> will simply tell users what your package is about.
## Step 5. Generate your source distribution
Once you have all the needed files, use the following command to install the latest version of the setuptools package (we used in the setup.py file).
```
python -m pip install --user --upgrade setuptools
```
Make sure you are at the same directory where setup.py is located and run this command:
```
python setup.py sdist
```
You will see there is a new folder dist containing the tar.gz file that provides metadata and the essential source files needed for installing by pip.
## Step 6. Create accounts for the Test PyPI and PyPI repositories.
Go to PyPI test and PyPI sites and create your accounts, it’s important to remember your passwords, those will be retyped into the command line very soon.
## Step 7. Upload your package to the Test PyPI repository
The next step is to install twine, this utility will help you to upload your package to the PyPI repository or other repositories. Once you have installed twine, you won’t need to repeat this step.
```
pip install twine
```
Open a terminal and type the command below in your command line, it will ask you to provide the user and password you created previously on step 6.
```
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```
Login to the Test PyPI repository and verify that your package is in there. If so, copy the command that is under the package’s name, run it in your command line and, read in your screen the message saying that your package was successfully installed.
```
pip install -i https://test.pypi.org/simple/ guesser-game
```
## Step 8. Upload your package to the PyPI repository
Finally, this is the last command you have to run to share your package with the worldwide community of Python developers. Make sure you are at the same directory where the setup.py file is located.
```
twine upload dist/*
```
Now, the package is in the PyPI repository!
```
pip install my-lib-bank-rate
```