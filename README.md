# retrieveOAImets

Retrieve the metadata of one or more resources in METS format from OAI-PMH data providers.

## Requirements
- IDs of the resources should be given in the input file.
- The input file should follow these rules: .txt format, one ID per line (see `exampleData`).
- Python3 should be installed on your computer. To check this, open a terminal and type `python`. If the answer starts with `Python 3.`, Python3 is installed (to get back to the terminal, type `exit()`). Otherwise, install it at https://www.anaconda.com/ or https://www.python.org/.

## Run the script
Open a terminal and run the file `retrieveOaiMetadataMets_parsingXML.py` adding as arguments
- the url of the OAI-PMH interface of the data provider, and
- the path to the input file.

		python retrieveOaiMetadataMets_parsingXML.py PROVIDER_URL FILE_PATH

For example
	
	python retrieveOaiMetadataMets_parsingXML.py https://oai.sbb.berlin/ exampleData/IDs_stabi.txt

Examples of input files are available in the dir `exampleData`.
	
For help

	python retrieveOaiMetadataMets_parsingXML.py --help

## Debugging
The code prints the ID before retrieving the correspondant metadata. If it breaks, check the last ID printed.

Error `sickle.oaiexceptions.CannotDisseminateFormat` means that the last ID printed out by the script is wrong.

