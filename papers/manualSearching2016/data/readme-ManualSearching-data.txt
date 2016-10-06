Readme for:
[TO UPDATE NAME OF DATA PACKAGE, AND ASSOCIATED PAPER]
Readme author and contact person: Matt Mayernik, mayernik@ucar.edu
Readme created: Oct. 6, 2016


SECTION 1 - METHOD 
Some of the information in this methods section, along with additional information, is included in the associated paper's methods section. This study uses four case studies to examine citation & reference patterns to different kinds of resources. 

– North American Regional Climate Change Assessment Program (NARCCAP) data set, DOI assigned 2012-05-03
– NCEP FNL Operational Model Global Tropospheric Analyses data set, DOI assigned 2014-01-30
– NCAR Command Language (NCL), DOI assigned 2012-04-10
– Yellowstone supercomputer, ARK assigned 2012-05-21

Literature searches were conducted using the Google Scholar search index between March-May 2016 to find papers that used these four resources. The search terms shown in Table 2 of the article were used to find papers that explicitly noted their use of these four  resources. 

Each document returned by Google Scholar for these search terms was then examined to identify whether the paper actually used the resource of interest, and if so, where in the paper the use of the resource was noted. Any duplicate documents returned by more than one of the above searches were removed to prevent double counting. This study did not count references that occurred in abstracts, posters, or presentations.

Each relevant document was coded with regard to whether the following reference types were present: 

Citation – inclusion of the resource in the reference list 
Acknowledgement – mention of the resource in the Acknowledgement section
In-text reference – mention of the use of the resource in the body text 

In the documents examined in this study, it was quite common for individual documents to include one, two, or all three of these reference types, in every possible combination. To reduce the complexity of coding for this variability in reference type combinations, the reference types were coded in priority order: 1) citations, 2) acknowledgements, and 3) In-text references. For example, in examining a relevant document for the NARCCAP data set, if a formal citation to the data set was present in the reference list, the document was coded as “citation”, whether or not the data set was also mentioned in the acknowledgements or body of the text. If a document included an acknowledgement to the NARCCAP data set but no formal citation, the document was coded as “acknowledgement,” whether or not the data set was also mentioned in the body of the text. Finally, if the usage of the NARCCAP data set was noted in the body of the text, with no formal citation or acknowledgement given, the document was coded as “in-text reference”. 

Each reference was also coded for the presence or absence of the persistent ID.

Finally, the relevant documents were then categorized into primary literature vs. grey literature, with the distinction as follows:

Primary literature – articles with DOIs, e.g. journal articles, some conference proceedings, some book chapters
Grey literature – documents without DOIs, e.g. conference proceedings, theses, pre-prints, etc.

The dates of publication for the relevant documents used to produce Figure 3 in the article were gathered by querying the DOI resolution server via a Python script to pull down the metadata associated with each document’s DOI. 


SECTION 2 - DATA FILE DESCRIPTIONS
Within the data file names and column headers, the names of the four case studies are abbreviated as follows:

NARCCAP
NCEP
NCL
Yellowstone

This collection includes eight data files. There are two data files for each of the four case studies. One file contains data about documents that reference the resource via the persistent identifier (DOI or ARK), and the other file contains data about documents that reference the resource by name (or in some other fashion without using the persisent ID). 

NARCCAP-DOI-Refs.csv - Data about documents that reference the NARCCAP data set via its DOI. 

NARCCAP-Name-Refs.csv - Data about documents that reference the NARCCAP data set by name or in some other fashion, without using the DOI. 

NCEP-DOI-Refs.csv - Data about documents that reference the NCEP data set via its DOI. 

NCEP-Name-Refs.csv - Data about documents that reference the NCEP data set by name or in some other fashion, without using the DOI. 

NCL-DOI-Refs.csv - Data about documents that reference the NCL software via its DOI. 

NCL-Name-Refs.csv - Data about documents that reference the NCL software by name or in some other fashion, without using the DOI. 

Yellowstone-ARK-Refs.csv - Data about documents that reference the Yellowstone Supercomputer via its ARK. 

Yellowstone-ARK-Refs.csv - Data about documents that reference the Yellowstone Supercomputer by name or in some other fashion, without using the ARK. 


SECTION 3 - DATA FILE STRUCTURE
Each of the eight data files has the same structure. Each data file has three columns:

Column 1 - "Doc-IDs"
This column lists the web-accessible identifiers for the documents that referenced the resource of interest. The identifiers included in the list consist of DOIs for primary literature and URLs for gray literature. This distinction is also coded in column 3 below. 

Column 2 - "Reference-Code"
The second column lists the type of reference included in the document identified in column 1. The reference types have been coded. Three codes are possible:

A - Acknowledgement
C - Citation
T - In-text reference

Column 3 - "Paper-Type"
This column lists the type of paper identified in column 1. As noted above, for this study, two paper types are used: Primary literature and gray literature. In this column, these types are coded as follows:

P - Primary literature
G - Gray literature



SECTION 4 - EXAMPLE
Here the first line of one data file is described as an example of the data structure and codes. In the file NARCCAP-DOI-Refs.csv, the first line (after the column header labels) is as follows:

10.1175/JAMC-D-13-0361.1,T,P

This means that the article with DOI "10.1175/JAMC-D-13-0361.1", in this case an article from the Journal of Applied Meteorology and Climatology, referenced the NARCCAP data set via an in-text reference (second column "T"). Because it is a journal article with a DOI, it is coded as "P" for "Primary literature" in the third column.

