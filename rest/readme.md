# Rest Eve Assignment

## Three API endpoints are provided.

* /processor : Returns below Json

		{
  			"ProcessorName": "i386", 
  			"Node": "Saurabhs-MacBook-Pro.local", 
  			"System Name": "Darwin", 
  			"Version": "Darwin Kernel Version 17.5.0: Mon 							Mar  5 22:24:32 PST 2018; 			root:xnu-4570.51.1~1/RELEASE_X86_64", 
  			"Release": "17.5.0"
		}
* /disk

		{
  			"Disk Used": 191147995136, 
  			"Disk Free": 56816381952, 
  			"Total Disk Size": 250790436864
		}
* /ram

		{
  			"Ram Free": 7431647232, 
  			"Total Ram": 17179869184, 
 			"Ram Used": 16965099520
		}

## Executing the micro service

* git clone the project and make sure rest eve is available in your enviornment
* run the run.py