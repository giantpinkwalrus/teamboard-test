## Robot Framework

Robot Framework is a generic test automation framework for acceptance testing and acceptance test-driven development (ATDD). 
It has easy-to-use tabular test data syntax and it utilizes the keyword-driven testing approach. 
Its testing capabilities can be extended by test libraries implemented either with Python or Java, and users can create new 
higher-level keywords from existing ones using the same syntax that is used for creating test cases. 

### How to install?
  There are many ways to install robot framework to your computer. 
  But here is Robot Frameworks own [installation instructions](https://github.com/robotframework/robotframework/blob/master/INSTALL.rst) or you can follow fast guide(shown below) how to install it. 
  
###Fast Guide to install Robot Framework
####1. Preconditions
Robot Framework is supported on Python, Jython (JVM) and IronPython (.NET)
and runs also on PyPy. The interpreter you want to use should be 
installed before installing the framework.
    
On most UNIX-like systems such as Linux and OS X you have Python installed by default. 
If you are on Windows or otherwise need to install Python yourself, 
a good place to start is [python.org](http://python.org).

On this guide we are using python, so the commands are for python.
   
####2. Installing Robot Framework
Easiest way to install Robot Framework is using package manager like [pip](https://pip.pypa.io/en/latest/index.html).

Install pip if you don't already have it installed.
```
sudo apt-get install python-pip
```
Using pip to install Robot Framework
```
# Install the latest version
pip install robotframework
```
Now you have Robot Framework installed! 


If you want use specific version of Robot Framework or upgrade it, 
you can use these commands:
```
# Upgrade to the latest version
pip install --upgrade robotframework

# Install a specific version
pip install robotframework==2.8.5

# Uninstall
pip uninstall robotframework
```
####3. Installing Selenium2Library for RobotFramework
[Selenium2Library](https://github.com/rtomac/robotframework-selenium2library) is a web testing library for Robot Framework. That you'll be using for creating tests.

Install Selenium2Library using pip
```
pip install robotframework-selenium2library
```
####4.Robot Framework is ready to use
Now you can start runnig test from your terminal. 

You can also use [RIDE](https://github.com/robotframework/RIDE/wiki) which is easy to use tool for running tests and creating tests


### How to run tests
Once you have Robot Framework in working condition you can run your tests using `pybot` command.

####1. Preconditions
These test are from Contriboard Testing folder. Before running them check that variables are correct for your Contriboard configuration.

Open resource.txt and edit these lines to match your Contriboard server url and user:
```
${ValidUser} testbaboon@test.com
${ValidPassword} t3stmonkey
${SERVER} localhost:8000
```
These hardcode users will be removed in the future

####2. Running tests

Run a test:
```
pybot New_User_Test.txt
```
Run all tests from folder:
```
pybot Contriboard Testing
```
### Useful links for creating tests

- [Robot Framework](http://robotframework.org/)
- [Robot Framework User Guide](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html)
- [Selenium2Library keywords](http://rtomac.github.io/robotframework-selenium2library/doc/Selenium2Library.html)
- [RF Builtin keywords](http://robotframework.org/robotframework/latest/libraries/BuiltIn.html)
- [RF Collections keywords](http://robotframework.org/robotframework/latest/libraries/Collections.html)

