# Genome Assembly, Annotation, and Metabolic Pathway Prediction

## Background

Microbial communities of bacteria form complex interactions in nature. However, our understanding of these communities that reside in humans and other animals is limited to those that can be cultured in the lab. In comparison to other microbiomes such as ones in soil or in the human gut, the human urinary tract (UT) harbors a lower biomass. Thus, this decreased diversity of the UT serves as an ideal model to delve into its interconnected nature, which has yet to be fully uncovered. This microbiome, which was previously thought to be sterile, hosts a diverse assortment of bacteria and other microbes that make up what is known as the urobiome. Enhanced culture methods have enabled the isolation of numerous fastidious species from the UT, definitively proving that the urinary tract of asymptomatic individuals is not sterile. To examine urobiome communities and their potential interactions metabolically, I computationally predicted metabolic pathways from bacterial genomes of a given patient's urine sample to determine if specific bacteria form dependent relationships in the urobiome for metabolic benefits.


## Overview

Bacterial genomes from patients that have multiple bacterial isolates sequenced were assembled using SPAdes v 3.15.2 via the Pathosystems Resource Integration Center (PATRIC) v. 3.6.12. Genome assemblies were also annotated using PATRIC. The features.txt file produced from each annotation was parsed via Python v.3.8.5 to extract the enzyme codes (EC) needed to generate metabolic maps using KEGG Mapper-Color; a web tool for metabolic pathway prediction.


## Software 

* Python3
* KEGG Mapper


## Genomes annotated



| Sample ID     | Patient ID    | Species      |
| ------------- | ------------- | ------------ | 
| Content Cell  | RUTISD6       | Staphylococcus epidermidis |
| Content Cell  | RUTISD6       | Klebsiella pneumoniae |
| Content Cell  | RUTISD6       | Klebsiella pneumoniae |
| Content Cell  | RUTISD6       | Lactobacillus gasseri |
| Content Cell  | RUTISD6       | Lactobacillus delbrueckii |
| Content Cell  | RUTISD6       | Enterococcus faecalis |
| Content Cell  | RUTISD9       | Klebsiella pneumoniae |
| Content Cell  | RUTISD9       | Enterococcus faecalis |
| Content Cell  | RUTISD9       | Staphylococcus epidermidis |  
| Content Cell  | RUTISD9       | Streptococcus agalactiae |
| Content Cell  | RUTISD9       | Klebsiella pneumoniae |
| Content Cell  | RUTISD9       | Lactobacillus jensenii | 
| Content Cell  | RUTISD018     | Escherichia coli |
| Content Cell  | RUTISD018     | Enterococcus faecalis |
| Content Cell  | RUTISD018     | Lactobacillus jensenii |
| Content Cell  | RUTISD018     | Lactobacillus gasseri |
| Content Cell  | RUTISD25      | Escherichia coli |
| Content Cell  | RUTISD25      | Streptococcus anginosus | 
| Content Cell  | RUTISD25      | Actinotignum sanguinis |
| Content Cell  | RUTISD25      | Aerococcus urinae |
| Content Cell  | RUTISD25      | Aerococcus sanguinicola |
| Content Cell  | RUTISD25      | Escherichia coli |






























