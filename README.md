## retrieveOAImets

This script 
- retrieves metadata in Mets format from OAI-PMH data providers
- write them to a tabular format

Open a terminal and run the file `retrieveOaiMetadataMets.py` adding as arguments the data provider and the id of the resource, like this:

	python retrieveOaiMetadataMets.py REPO-URL ID

For example
	
	python retrieveOaiMetadataMets.py https://www.e-rara.ch/oai 8965440
	
For help

	python retrieveOaiMetadataMets.py --help

