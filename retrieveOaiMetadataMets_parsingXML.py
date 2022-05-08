import argparse
import urllib3
from lxml import etree
import csv
import os

################# PARSE THE ARGUMENT #####################
parser = argparse.ArgumentParser()
parser.add_argument('provider_url', action='store', help="the url of the OAI-PMH interface of the data provider")
parser.add_argument('file_path', action='store', help="the path to the file where the IDs of the resources are listed")
args = parser.parse_args()


################# RETRIEVE THE LIST OF IDs FROM THE INPUT FILE #################
fileIn = open(args.file_path, "r")
IDs_list = [line[:-1] for line in fileIn]


# name of csv output file
if not os.path.exists('results'):
    os.makedirs('results')
providerName = args.provider_url.replace("https://", "").replace("/", "") 
filename = "results/metsDocs_" + providerName + ".csv"

# open csv output file and write the headers row
with open(filename, 'w') as csvfile: 

    # create a csv writer object 
    csvwriter = csv.writer(csvfile, delimiter =';',quotechar ='"') 
    # define the field headers 
    fields = ['Internal ID', 'Title', 'Alternative title', 'Place', 'Publisher', 'Date', 'Extent', 'Language', 'Biblio', 'Internal related item', 'Access, use and reproduce conditions', 'Presentation', 'IIIF manifest', 'Internal reference']
    # write the fields header
    csvwriter.writerow(fields) 


    ################# For each ID in the input file
    for short_id in IDs_list:
        print(short_id) ## print the ID, so in case of problems we know where it brakes
        
        ################# Access the XML online
        http = urllib3.PoolManager()
        r = http.request('GET', args.provider_url + '?verb=GetRecord&metadataPrefix=mets&identifier=' + short_id)
        # print(r.status)
        xml_content = r.data

        ################# Parse the XML
        root = etree.XML(xml_content)

        # there is a shorter syntax for namespaces using the xpath method, but from the lxml doc: The .find*() methods are usually faster than the full-blown XPath support.
        # the .find method only returns the first occurrence, otherwise use .findall. Here sometimes we have multiple items in one document, but looking at the results in most cases we only need the first, so it is a pragmatic decision to use .find       
        
        firstDocOnly = root.find(".//{http://www.loc.gov/METS/}dmdSec") # take only the first <mets:dmdSec> (descriptive metadata section)

        def findOptionalElementsText(xpath):
            if (firstDocOnly.find(xpath) != None): # check if the element appears in the doc
                elements = firstDocOnly.findall(xpath)  # find all occurrences
                elementsList = [] # else create a list
                for x in elements:
                    elementsList.append(x.text)  # populate the list with the textual content of the elements
                return str(elementsList).replace("['", "").replace("']", "").replace("', '", "\n").replace("[", "").replace("]", "")  # print as string, one item per line
            else:
                return "NONE"





        modsTitle = firstDocOnly.findtext(".//{http://www.loc.gov/mods/v3}titleInfo/{http://www.loc.gov/mods/v3}title")

        modsBiblio = findOptionalElementsText(".//{http://www.loc.gov/mods/v3}note[@type='bibliography']")
        
        modsAlternativeTitle = findOptionalElementsText(".//{http://www.loc.gov/mods/v3}titleInfo[@type='alternative']/{http://www.loc.gov/mods/v3}title")

        modsPlaceTerm = findOptionalElementsText(".//{http://www.loc.gov/mods/v3}originInfo//{http://www.loc.gov/mods/v3}placeTerm")

        modsDateIssued = findOptionalElementsText(".//{http://www.loc.gov/mods/v3}originInfo//{http://www.loc.gov/mods/v3}dateIssued")

        modsPublisher = findOptionalElementsText(".//{http://www.loc.gov/mods/v3}publisher")

        modsRelatedItem = findOptionalElementsText(".//{http://www.loc.gov/mods/v3}relatedItem[@type='original']//{http://www.loc.gov/mods/v3}recordIdentifier")
        
        modsLanguage = findOptionalElementsText(".//{http://www.loc.gov/mods/v3}language/{http://www.loc.gov/mods/v3}languageTerm")

        modsExtent = findOptionalElementsText(".//{http://www.loc.gov/mods/v3}physicalDescription/{http://www.loc.gov/mods/v3}extent")

        modsAccessCondition = findOptionalElementsText(".//{http://www.loc.gov/mods/v3}accessCondition")
        
        dvInternalRef = root.findtext(".//{http://dfg-viewer.de/}reference")

        dvPresentation = root.findtext(".//{http://dfg-viewer.de/}presentation")
        
        dvIIIF = root.findtext(".//{http://dfg-viewer.de/}iiif")


        ################# Populate the row and write it to file
        row = [short_id, modsTitle, modsAlternativeTitle, modsPlaceTerm, modsPublisher, modsDateIssued, modsExtent, modsLanguage, modsBiblio, modsRelatedItem, modsAccessCondition, dvPresentation, dvIIIF, dvInternalRef] 
        csvwriter.writerow(row)

