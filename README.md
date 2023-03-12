# Genome Assembly, Annotation, and Metabolic Pathway Prediction

## Background

Microbial communities of bacteria form complex interactions in nature. However, our understanding of these communities that reside in humans and other animals is limited to those that can be cultured in the lab. In comparison to other microbiomes such as ones in soil or in the human gut, the human urinary tract (UT) harbors a lower biomass. Thus, this decreased diversity of the UT serves as an ideal model to delve into its interconnected nature, which has yet to be fully uncovered. This microbiome, which was previously thought to be sterile, hosts a diverse assortment of bacteria and other microbes that make up what is known as the urobiome. Enhanced culture methods have enabled the isolation of numerous fastidious species from the UT, definitively proving that the urinary tract of asymptomatic individuals is not sterile. To examine urobiome communities and their potential interactions metabolically, I computationally predicted metabolic pathways from bacterial genomes of a given patient's urine sample to determine if specific bacteria form dependent relationships in the urobiome for metabolic benefits.


## Overview

Bacterial genomes from patients that have multiple bacterial isolates sequenced were assembled using SPAdes v 3.15.2 via the Pathosystems Resource Integration Center (PATRIC) v. 3.6.12. Genome assemblies were also annotated using PATRIC. The features.txt file produced from each annotation was parsed via Python v.3.8.5 to extract the enzyme codes (EC) needed to generate metabolic maps using KEGG Mapper-Color; a web tool for metabolic pathway prediction.


## Software 

* Python3
* [KEGG Mapper-Color](https://www.genome.jp/kegg/mapper/color.html)


## Genomes annotated



| Sample ID     | Patient ID    | Species      |
| ------------- | ------------- | :------------ | 
| 512           | RUTISD6       | Staphylococcus epidermidis |
| 610           | RUTISD6       | Klebsiella pneumoniae |
| 946           | RUTISD6       | Klebsiella pneumoniae |
| 612           | RUTISD6       | Lactobacillus gasseri |
| 615           | RUTISD6       | Lactobacillus delbrueckii |
| 617           | RUTISD6       | Enterococcus faecalis |
| 441           | RUTISD9       | Klebsiella pneumoniae |
| 442           | RUTISD9       | Enterococcus faecalis |
| 443           | RUTISD9       | Staphylococcus epidermidis |  
| 444           | RUTISD9       | Streptococcus agalactiae |
| 445           | RUTISD9       | Klebsiella pneumoniae |
| 446           | RUTISD9       | Lactobacillus jensenii | 
| 479           | RUTISD018     | Escherichia coli |
| 102           | RUTISD018     | Enterococcus faecalis |
| 482           | RUTISD018     | Lactobacillus jensenii |
| 483           | RUTISD018     | Lactobacillus gasseri |
| 530           | RUTISD25      | Escherichia coli |
| 531           | RUTISD25      | Streptococcus anginosus | 
| 532           | RUTISD25      | Actinotignum sanguinis |
| 533           | RUTISD25      | Aerococcus urinae |
| 535           | RUTISD25      | Aerococcus sanguinicola |
| 536           | RUTISD25      | Escherichia coli |






























