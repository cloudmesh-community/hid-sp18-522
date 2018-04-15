# Swagger Codegen Assignment: Implemented an API to Download and visualize Iris DataSet
  
## Usage of Files and Data Structures using rest services hid-sp18-522

* Pandas (open source, BSD-licensed library providing
  high-performance, easy-to-use data structures and data analysis
  tools for the Python programming language) is used to
  manipulate the Iris dataset available on
  <https://archive.ics.uci.edu/ml/machine-learning-databases/iris/>

* This Iris dataset contains 150 instances with 3 classes of 50 instances each, where each class refers to a type of iris plant.


* Three API endpoints are provided.

  * ```/Iris/Download```
  
  * ```/Iris/categories```
  
  * ```/Iris/categories/categoryname```
  
 

## Instructions for docker installation

* git clone the project.

* you should install docker.

* change the directory to **swagger** folder.

* Build the image from docker file

	* ``` make docker-build ```

* Start the service using following make command
  
  * ```make docker-start```

* Test the service using following curl commands
  
  
  * ```curl -H "Content-Type:application/json" -X GET http://localhost:8080/Iris/Download```
  
  * ```curl -H "Content-Type:application/json" -X GET http://localhost:8080/Iris/categories```     
  
  
  * ```curl http://127.0.0.1:8080/Iris/categories/categoryname (Categoryname should be either of the categories returned by Iris/categories endpoint)```

  
  

* Get the container ID using following command
  
  * ```docker ps```

* Stop the service using following commands
  
  * ```make docker-stop```

* Optional starting mechanism (interactive mode)
  
  * ```make start``` 
  
  * ```make stop```
	
## Instructions for ubuntu without docker

* you should be running this program in python 2 environment.

* you should have default-jre installed.

* git clone the project.

* change the directory to swagger folder

* Ensure Python 2 environment is activated

	* ``` pyenv activate env2 (Refer handbook for details ```

* create the swagger server with following command
  
  * ```make service```

* run the swagger server with following command
  
  * ```make start```

* test the program using following command
  
  * ```make test-download```
  
  * ```make test-categories```
  
  * ```make test-categoryname```

* stop the service using following command
  
  * ```make stop```

* clean the server and client codes using following command
  
  * ```make clean```

## API informations : Data Services

### End Point : Iris/Download
  
  * This endpoint access the url where Iris dataset is available and downloads the csv datafile to the server using the url
 
  * Sample curl request
  
	  ```curl -H "Content-Type:application/json" -X GET http://localhost:8080/Iris/Download ```
  
  * Sample json response for GET request 
  
	```
	Download {
		model:	
			string *
	}

	```

### End Point : Iris/categories
  
  * The endpoint returns all three unique Iris flower class names 
  
  * Sample curl request
  
	  ```curl -H "Content-Type:application/json" -X GET http://localhost:8080/Iris/categories ```
 
  * Sample json response for GET request
  
	```
	[
		IrisCategories {
			categories:	
				string *
		}
	]

	```
### End Point : Iris/categories/categoryname

* The endpoint returns all data for categoryname provided 

* Sample curl request
	  
	  ```curl -H "Content-Type:application/json" -X GET http://localhost:8080/Iris/categories/categoryname (Categoryname should be either of the categories returned by Iris/categories endpoint) ```

 * Sample json response for GET request
 	
 	``` 
 		[
			IrisDisplay {
				petallength:	
					string *
				petalwidth:	
					string *
				sepallength:	
					string *
				sepalwidth:	
					string *
				name:	
					string *
			}
		]

	```
