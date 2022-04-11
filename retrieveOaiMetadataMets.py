
# sickle is a OAI-PMH Python client library, more at https://pypi.org/project/Sickle/
# an alternative is https://pypi.org/project/pyoai/
# See https://xennis.org/wiki/Python_-_OAI-PMH for an example of both


from sickle import Sickle
import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('repo', action='store', help='for example https://www.e-rara.ch/oai')
parser.add_argument('id', action='store', help='for example 8965440')
args = parser.parse_args()

repo_url = args.repo
short_id = args.id



################# GET RECORD #################
sickle = Sickle(repo_url)
record = sickle.GetRecord(identifier=short_id, metadataPrefix='mets')

header = record.header
record_id = header.identifier

metadata = record.metadata
if 'title' in metadata:
    record_title = str(metadata['title'])[2:-2] # converting to string and slicing to remove the [''] for each list
else: record_title = "NO DATA"

if 'creator' in metadata:
    record_creator = str(metadata['creator'])[2:-2]
else: record_creator = "NO DATA"

if 'tableOfContents' in metadata:
    record_description = str(metadata['tableOfContents'])[2:-2]
else: record_description = "NO DATA"

if 'placeTerm' in metadata:
    record_place = str(metadata['placeTerm'])[2:-2]
else: record_place = "NO DATA"

if 'publisher' in metadata:
    record_publisher = str(metadata['publisher'])[2:-2]
else: record_publisher = "NO DATA"

if 'dateIssued' in metadata:
    record_date = str(metadata['dateIssued'])[2:-2]
else: record_date = "NO DATA"

if 'extent' in metadata:
    record_format = str(metadata['extent'])[2:-2]
else: record_format = "NO DATA"

if 'identifier' in metadata:
    record_identifier = str(metadata['identifier'])[2:-2]
else: record_identifier = "NO DATA"

if 'url' in metadata:
    record_doi = str(metadata['url'])[2:-2]
else: record_doi = "NO DATA"

if 'presentation' in metadata:
    record_presentation = str(metadata['presentation'])[2:-2]
else: record_presentation = "NO DATA"

if 'iiif' in metadata:
    record_iiif = str(metadata['iiif'])[2:-2]
else: record_iiif = "NO DATA"

if 'languageTerm' in metadata:
    record_language = str(metadata['languageTerm'])[2:-2]
else: record_language = "NO DATA"

if 'license' in metadata:
    record_rights = str(metadata['license'])[2:-2]
else: record_rights = "NO DATA"

if 'reference' in metadata:
    record_reference = str(metadata['reference'])[2:-2]
else: record_reference = "NO DATA"


# field names 
fields = ['ID', 'Title', 'Creator', 'Description', 'Place', 'Publisher', 'Date', 'Format',  'Language', 'Rights', 'Identifier', 'DOI', 'Presentation', 'IIIF manifest', 'Owner reference'] 
    
# data row of csv file 
row = [record_id, record_title, record_creator, record_description, record_place, record_publisher, record_date, record_format, record_language, record_rights, record_identifier, record_doi, record_presentation, record_iiif, record_reference] 
    
# name of csv file 
filename = "oaiMets_" + short_id + ".csv"

    
# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(fields) 
        
    # writing the data rows 
    csvwriter.writerow(row)