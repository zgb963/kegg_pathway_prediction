
#Process_file function takes in an input folder (aim3meta with .features.txt files for 22 genome annotations)
#Construct code to read through all files in folder. Call function at end of function, passing in different input/output/color to each call


import re #re=regular expression specifies a set of strings that matches it. Check if a particular string matches a given regular expression

import glob #run trhough aim3meta folder

path='/Users/genevievebaddoo/aim3meta' #where all features.txt files are for each bacterial species

files = glob.glob(path + '/*') #walk through ALL .features.txt files in  aim3meta folder and run function for each file


def process_file(input_file,output_file,color): #3 parameters/arguments of function: input_file = features.txt, output_file = ec list, color (want to make different for each file) (max 6 colors)
    with open(input_file) as f:
        x=f.readlines()
    
    ECs=set() #ecs=enxyme codes. Keep in a set, which is a an unordered and mutable collection of unique elements in {}
    for i in x[1:]:
        y=i.split('\t')
        if '(EC ' in y[3]:
            z=re.findall('\(.*?\)',y[3]) #find all enxyme codes in .txt file
            for j in z:
                if j.startswith('(EC '):
                    ECs.add(j[4:-1]) #add to list of ECs
            
    #output format EC number and color (separated by space)
    with open(output_file,'w') as f:
        for i in ECs:
            f.write(i+' '+color+'\n') #list of EC's and color in the features.txt_results


for i in files: #for the number of files in aim3meta folder
    process_file(i , i + '_results', 'magenta') #cal the function above, i = number of files in aim3meta folder, i + '_results' to differentiate between the files, 'red' = color
    
    
            

