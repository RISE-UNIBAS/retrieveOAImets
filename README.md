## retrieveOAImets

Retrieve the metadata in METS format from OAI-PMH data providers of one or more resources.

**Requirements**
- IDs of the resources should be given in the input file.
- The input file should be structured as following: .txt format, the ID of the resource, one per line (see below for an example).
- Python3 should be installed on your computer. To check this, open a terminal and type `python`. If the answer starts with `Python 3.`, Python3 is installed (to get back to the terminal, type `exit()`). Otherwise, install it at https://www.anaconda.com/ or https://www.python.org/.


#### Run the script
Open a terminal and run the file `retrieveOaiMetadataMets_parsingXML.py` adding as arguments the url of the OAI-PMH interface of the data provider and the path to the input file:

	python retrieveOaiMetadataMets_parsingXML.py PROVIDER_URL FILE_PATH

For example
	
	python retrieveOaiMetadataMets_parsingXML.py https://oai.sbb.berlin/ exampleData/IDs_stabi.txt

Examples of input file are available in the dir `exampleData`.
	
For help

	python retrieveOaiMetadataMets.py --help

#### Debugging
The code prints the ID before retrieving the correspondant metadata. If it breaks, check the last ID printed.

Error `sickle.oaiexceptions.CannotDisseminateFormat` means that the last ID printed out by the script is wrong.

