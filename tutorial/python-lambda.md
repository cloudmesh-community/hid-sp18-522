# Python Lambda Expressions: 

**Lambda Expressions** are inline anonymous functions which don't require explicit definition. These expressions substitute for named python functions. They are useful when some really simple function usually having a single expression is required and which is used only once within the program. Using Lambda expression in such cases makes code easy and clean.

**Lambda expressions** start with a key word Lambda followed by inputs and then colon. After colon is the expression which has a return value. Below example shows a lambda expression which takes X as input and returns x^2 - 3x + 2.

## Single Input Lambda Expression Example:

Lambda X: X^2 - 3X + 2 

As Lambda expression doesn't have name as they are anonymous function, to call them they can be assigned to a variable and called through that as shown below.

Y = Lambda X: X^2 ? 3X + 2 

## Multiple Input Lambda Expression Example:

Lambda X,Y: X+Y

## Some key features of Lambda Expressions:

-	Lambda Expressions can take multiple inputs x1, x2..xn
-	Lambda Expressions must have single expression which must return a value
-	Assignment Statements can?t be used
-	Lambda Expressions can?t be used for multiline functions
-	They can be used to build quadratic functions which can be eventually returned from some function.
-	List comprehensions can be converted to Lambda by removing squared brackets


# Python nosetests:

Nose Test is a testing framework for python. It takes all testing modules from unittest.TestCase class which is an instance of python TestClass. Apart from the functions provided by UnitTest class, custom test functions can also be written. 

Python NoseTest comes bundled with several helpful functions for writing timed test and exception tests. Multiple tests are group of functions which as per standard begin with test_. For all the failed tests, nose returns F and . for all successful ones. The documentation for testing with Nose can be found [here](http://nose.readthedocs.io/en/latest/writing_tests.html)

## Installing Nose:

Pip install nose 

## Writing Test:

Nose Tests are not required to inherit the class unittest.TestCase unlike PyTest. Classes having following properties can be run as test.

-	Matches configured test Match regular expression ((?:^|[\\b_\\.-])[Tt]est by default ?
-	Has test or Test at a word boundary
-	Present in the same module that matches that expression

## Test Packages:

Nose allows testes to be grouped into test packages. This allows package-level setup; for instance, if you need to create a test database or other data fixture for your tests, you may create it in package setup and remove it in package teardown once per test run, rather than having to create and tear it down once per test module or test case?

## Test modules:

A test module is a python module that matches the testMatch regular expression. Test modules offer module-level setup and teardown; define the method setup, setup_module, setUp or setUpModule for setup, teardown, teardown_module, or tearDownModule for teardown. Execution of tests in a test module begins after all tests are collected.

## Test classes:
A test class is a class defined in a test module that matches testMatch or is a subclass of unittest.TestCase. All test classes are run the same way: Methods in the class that match testMatch are discovered, and a test case is constructed to run each method with a fresh instance of the test class

## Test functions:
Any function in a test module that matches testMatch will be wrapped in a FunctionTestCase and run as a test. The simplest possible failing test is therefore

def test():
    assert False

And the simplest passing test:

def test():
    pass

## Running Nose: 

nosetests command is used to run the nose.

nosetests test_nosetestfile.py

# Python Generators

Generator is a way to create a function which can be used as an Iterator. In a function definition, return statement basically returns the value or list of values. After return statement executes, that function along with all local variables are destroyed. 
In Generators Yield keyword is used in place of return and the function state is preserved after its completion.

Two prominent benefits of using generators are Memory usage and Performance. Unlike List generators don't store results in memory but it creates an Iterator object. This provides a great performance boost if the data is huge.

## Example of using Generator:

def num_square(nums):
	for I in nums:	
		yield(i*i)
nums = num_square([2,4,67,89,99])

for num in my_nums:
	print num


# Python beautiful soup

Beautiful soap is a python library to parse HTML and used for Web scrapping. Three most powerful features of beautiful soup are: [Reference](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

1.	Beautiful Soup provides a few simple methods and Pythonic idioms for navigating, searching, and modifying a parse tree: a toolkit for dissecting a document and extracting what you need. It doesn't take much code to write an application
2.	Beautiful Soup automatically converts incoming documents to Unicode and outgoing documents to UTF-8. You don't have to think about encodings, unless the document doesn't specify an encoding and Beautiful Soup can't detect one. Then you just have to specify the original encoding.
3.	Beautiful Soup sits on top of popular Python parsers like lxml and html5lib, allowing you to try out different parsing strategies or trade speed for flexibility.

## Installing Beautiful Soup:

PIP INSTALL Beautifulsoup4

## Installing a parser:

Beautiful Soup supports the HTML parser included in Python?s standard library, but it also supports a number of third-party Python parsers. One is the lxml parser

pip install lxml

## Making the Soup:

To parse a document, pass it into the Beautiful Soup constructor

from bs4 import BeautifulSoup

with open("index.html") as fp:
    soup = BeautifulSoup(fp)

soup = BeautifulSoup("<html>data</html>")

First, the document is converted to Unicode, and HTML entities are converted to Unicode characters. Beautiful Soup then parses the document using the best available parser. It will use an HTML parser unless you specifically tell it to use an XML parser



# Python XML Parsing

**XML** stands for Extensible markup language. Python provides XML processing interfaces in xml package.

Modules in the xml package require that there be at least one SAX-compliant XML parser available.

## XML Handling sub modules can be broadly classified as below:

### 1) ElementTree XML API (xml.etree.ElementTree): [Reference](https://docs.python.org/2/library/xml.etree.elementtree.html)
This module converts XML hierarchical structure to tree. ElementTree represents the whole XML document as Tree and Element represents a single node in this tree. Interactions with the whole document are usually done on the ElementTree level. Interactions with a single XML element and its sub-elements are done on the Element level.

**Parsing XML:** 

Reading the file and getting the root

import xml.etree.ElementTree as ET

tree = ET.parse(?sample_xml_file.xml')
root = tree.getroot()

Reading the data from a string:

root = ET.fromstring (sample_data_as_string)

### 2) DOM API (xml.dom): [Reference](https://docs.python.org/2/library/xml.dom.html)

A DOM (Document Object Model) implementation represents an XML document as a tree structure or allows client code to build such a structure from scratch. It then gives access to the structure through a set of objects which provided well-known interfaces.

**DOM Module contents:**

**xml.dom. registerDOMImplementation (name, factory):** Register the factory function with the name 'name'. The factory function should return an object which implements the DOMImplementation interface. The factory function can return the same object every time, or a new one for each call, as appropriate for the specific implementation (e.g. if that implementation supports some customization)

**xml.dom. getDOMImplementation ([name [, features]]):** Return a suitable DOM implementation. If no name is given, and if the environment variable PYTHON_DOM is set, this variable is used to find the implementation

**Objects in DOM:** 

**DOMImplementation Objects:** The DOMImplementation interface provides a way for applications to determine the availability of particular features in the DOM they are using.

**Node Objects:** All of the components of an XML document are subclasses of Node

**NodeList Objects:** A NodeList represents a sequence of nodes. These objects are used in two ways in the DOM Core recommendation: an Element object provides one as its list of child nodes, and the getElementsByTagName () and getElementsByTagNameNS () methods of Node return objects with this interface to represent query results.

**DocumentType Object:** Information about the notations and entities declared by a document is available from a DocumentType object. The DocumentType for a document is available from the Document    object?s doctype attribute; if there is no DOCTYPEdeclaration for the document, the document?s doctype attribute will be set to None instead of an instance of this interface

**Document Object:** A Document represents an entire XML document, including its constituent elements, attributes, processing instructions, comments etc. Remember that it inherits properties from Node.

**Element Object:** Element is a subclass of Node, so inherits all the attributes of that class.

**Attr Object:** Attr inherits from Node, so inherits all its attributes.

**NamedNodeMap Object:** There are also experimental methods that give this class more mapping behavior. You can use them or you can use the standardized getAttribute* () family of methods on the Element objects.


**Comment Objects:** Comment represents a comment in the XML document. It is a subclass of Node, but cannot have child nodes.

**Text and CDATASection Objects:** The Text interface represents text in the XML document. If the parser and DOM implementation support the DOM?s XML extension, portions of the text enclosed in CDATA marked sections are stored in CDATASection objects. These two interfaces are identical, but provide different values for the nodeTypeattribute

**ProcessingInstruction Objects:** Represents a processing instruction in the XML document; this inherits from the Node interface and cannot have child nodes.

**Exceptions:**  The DOM Level 2 recommendation defines a single exception, DOMException, and a number of constants that allow applications to determine what sort of error occurred. DOMException instances carry a code attribute that provides the appropriate value for the specific exception.
The Python DOM interface provides the constants, but also expands the set of exceptions so that a specific exception exists for each of the exception codes defined by the DOM. The implementations must raise the appropriate specific exception, each of which carries the appropriate value for the code attribute.

### 3. SAX API (xml.sax): [Reference](https://docs.python.org/2/library/xml.sax.html)

The xml.sax package provides a number of modules which implement the Simple API for XML (SAX) interface for Python.

A typical SAX application uses three kinds of objects: readers, handlers and input sources. ?Reader? in this context is another term for parser, i.e. some piece of code that reads the bytes or characters from the input source, and produces a sequence of events. The events then get distributed to the handler objects, i.e. the reader invokes a method on the handler. A SAX application must therefore obtain a reader object, create or open the input sources, create the handlers, and connect these objects all together. As the final step of preparation, the reader is called to parse the input. During parsing, methods on the handler objects are called based on structural and syntactic events from the input data.

**SAX Functions:**

**xml.sax.make_parser:** Create and return a SAX XMLReader object. The first parser found will be used. If parser_list is provided, it must be a sequence of strings which name modules that have a function named create_parser(). Modules listed in parser_list will be used before modules in the default list of parsers.

**xml.sax.parse:** Create a SAX parser and use it to parse a document. The document, passed in as filename_or_stream, can be a filename or a file object. The handlerparameter needs to be a SAX ContentHandler instance.

**xml.sax.parseString:** Similar to parse(), but parses from a buffer string received as a parameter



# Python SQLite:

**SQLite** is used by small or medium size applications that needs database which may resides on disk. It is part of standard python library and can be used easily without any installation. Through SQLite we can create a database in a file or in memory.

To use SQLite3 python module, Connection object needs to be created which basically represent the database. Here is the basic code.

## Create DB in file using SQLite:

import sqlite3
conn = sqlite3.connect(':memory:')

**Next step after Connection is creating a Cursor object. Calling Execute method over Curser object is used for executing SQL commands.**

cursor = conn.cursor()

## Execute SQL commands
cursor.execute (??? CREATE TABLE Employee (first text, last text, pay integer)???)

## Commit changes
conn.commit()

## Close Connection.
conn.close()






