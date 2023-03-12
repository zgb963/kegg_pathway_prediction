# Genome Assembly, Annotation, and Metabolic Pathway Prediction

## Background

Microbial communities of bacteria form complex interactions in nature. However, our understanding of these communities is limited to those that can be cultured in the lab. Enhanced culture methods have enabled the isolation of numerous fastidious species from urinary tract, definitively proving that the urinary tract of asymptomatic individuals is not sterile. In working with these isolates, our group observed several instances in which a “purified” isolate harbors more than one species. We refered to these additional members as bacterial hitchhikers, a term previously used to describe similar occurrences in soil communities. I hypothesized that under a given culture condition, these bacterial hitchhikers would proliferate such that they could be isolated. Here, I computationally predicted metabolic pathways from bacterial genomes of a given patient's urine sample.


## Overview

Bacterial genomes from patients that have multiple bacterial isolates sequenced were assembled using SPAdes v 3.15.2 via the Pathosystems Resource Integration Center (PATRIC) v. 3.6.12. Genome assemblies were also annotated using PATRIC. The features.txt file produced from each annotation was parsed via Python v.3.8.5 to extract the enzyme codes (EC) needed to generate metabolic maps using KEGG Mapper-Color; a web tool for metabolic pathway prediction.


## Software 

* Python3
* KEGG Mapper

| First Header  | Second Header |
| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |
