# Shutterfly Coding Challenge
	Shutterfly code challange for data engineer role
	
# Shutterfly Customer Lifetime Value
One way to analyze acquisition strategy and estimate marketing cost is to calculate the Lifetime Value (“LTV”) of a customer. Simply speaking, LTV is the projected revenue that customer will generate during their lifetime.
A simple LTV can be calculated using the following equation:52(a) x t. Where a is the average customer value per week (customer expenditures per visit (USD) x number of site visits per week) and t is the average customer lifespan. The average lifespan for Shutterfly is 10 years.

# How to execute the code

 	• Change the “TOP_X_LTV_REPORT” value (currently set to 5) to execute the top X records
	• Run the src/ltv_report.py file
	• We should be seeing the output in output/output.txt location

	
# Source code Structure
[input/input.txt](https://github.com/ravikirandiwakarla/Shutterfly_Code_Challenge/blob/master/input/input.txt) : test data present here

[output/output.txt](https://github.com/ravikirandiwakarla/Shutterfly_Code_Challenge/tree/master/output) : test output will be saved

[sample_input/events.txt](https://github.com/ravikirandiwakarla/Shutterfly_Code_Challenge/blob/master/sample_input/events.txt) : sample data provided by Shutterfly

[src/models](https://github.com/ravikirandiwakarla/Shutterfly_Code_Challenge/blob/master/src/models.py ) : customer, image , site_visits and order models exist here

[src/constants.py](https://github.com/ravikirandiwakarla/Shutterfly_Code_Challenge/blob/master/src/constants.py) : place to store all the constant values

[src/common_util.py](https://github.com/ravikirandiwakarla/Shutterfly_Code_Challenge/blob/master/src/common_util.py) : utility to store common reusable functions

[src/file_util.py](https://github.com/ravikirandiwakarla/Shutterfly_Code_Challenge/blob/master/src/file_util.py) :  utilty to store file IO functions

[src/ingest.py](https://github.com/ravikirandiwakarla/Shutterfly_Code_Challenge/blob/master/src/ingest.py) : ingestion happens,responsible for ingestion the data into appropriate lists and dictionaries

[src/ltv_report.py](https://github.com/ravikirandiwakarla/Shutterfly_Code_Challenge/blob/master/src/ltv_report.py) : this is the starting point,generate_ltv_report method invokes all the functions to get the LTV report

[tests/test_files/test_bad_file.txt](https://github.com/ravikirandiwakarla/Shutterfly_Code_Challenge/blob/master/tests/test_files/test_bad_file.txt) : bad test file used for testing to test json exceptions

[tests/test_files/test_good_file.txt](https://github.com/ravikirandiwakarla/Shutterfly_Code_Challenge/blob/master/tests/test_files/test_good_file.txt) : good test file used for calculating LTV

[tests/test_common_util.py](https://github.com/ravikirandiwakarla/Shutterfly_Code_Challenge/blob/master/tests/test_common_util.py) : has the tests related to common_util.py file

[tests/test_file_util.py](https://github.com/ravikirandiwakarla/Shutterfly_Code_Challenge/blob/master/tests/test_file_util.py): has the tests related to file_util.py file

[tests/test_ltv_report.py](https://github.com/ravikirandiwakarla/Shutterfly_Code_Challenge/blob/master/tests/test_ltv_report.py) : has the tests related to ltv_report.py file

# Design Considerations
	• Each event will be ingested in their respective DTO’s list. Image event and most of the fields were not used to calculate the LTV but still stored as the 	      FAQ says we have to still ingest it as it can be useful for future analysis.
	• Couple of dictionaries - one for amount spent per customer and other for number of site visits are used for O(1) retrieval
	• While ingesting , based on the event, code updates the DTO list and dictionaries
	• To make sure the application continues gracefully for unexpected output, below considerations taken
		• If the amount spent is blank , considered value as 0
		• Site Visit per customer is considered at-least once if the customer event exists
	• Functionalities are segregated into separate files for easy maintenance
	• Verb such as New and update might have some importance but ignored currently
	• Tests were also segregated for easy maintenance and extendabilty

# Future Improvements
 	• As of now, we only used json structure and text extensions for input and output, but we can easily extend 
	  to other structured/semi structured formats and other extensions without changing the existing data structures.
 	• We can use this data to calculate the other metrics not limiting only to LTV
	• We might get some anomalies in our data or more bad data, app should be able to consider/exclude it wisely
	• We can hook this to streaming application to build real time values
		 
         







