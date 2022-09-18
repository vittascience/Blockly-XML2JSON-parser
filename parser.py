'''
 * @author [Taha NOUMAR]
 * @email [taha@vittascience.com]
 * @create date 2022-09-14 17:27:49
 * @modify date 2022-09-14 17:27:49
 * @desc [Python parser for XML blockly files -> generates a JSON file for, originally translation purposes]
'''

import re, json

#defining paths
dir_path = "./dir/"
original_file = dir_path + "original.js"  #original js file path containing XML variable (typicall en.js)
temp_file = dir_path + "temp.json"  # generated JSON file from original XML file
processed_file = dir_path + "processed.json"  # processed temp.json file (typically after translating it by a 3rd-party process)
output_file = dir_path + 'output.js'  #output translated JS file containing the translated XML data

#read file and store its content in variable
with open(original_file, "r", encoding="utf-8") as js_file:
    big_string = js_file.read()

#parse attributes from xml using regex
attribute_list = re.findall(r'"(.*?)"', big_string)

#split titles and attributes
titles = []
attributes = []
for index, string in enumerate(attribute_list):
    #titles have even index, attributes have odd indexes
    if index % 2 == 0:
        titles.append(string)
    else:
        attributes.append(string)
    #print(index, string)
#print(titles)
#print(attributes)

assert (len(titles) == len(attributes)
        )  # check if both lists have the same length
#build a dict using titles and attributes
my_dict = {}
for key in titles:
    for value in attributes:
        my_dict[key] = value
        attributes.remove(value)
        break
#print(my_dict)

#dump dict to json file
with open(temp_file, 'w', encoding="utf-8") as outfile:
    json.dump(my_dict, outfile, ensure_ascii=False)

# to be completed below
# add code snippet for Gtrad api for JSON file translation
print("Generated JSON file ready to be processed: " + temp_file)
#suppose translation is done

#open translated file & read translated file
with open(processed_file, "r", encoding="utf-8") as js_file:
    translated_data_dict = json.load(js_file)

#open output file
with open(output_file, 'r', encoding="utf-8") as outputfile:
    filedata = outputfile.read() # read content of the output file
    if filedata == "":
        filedata=big_string # duplicate the original file in the output file 

for _, (k, v) in enumerate(translated_data_dict.items()):
    # Replace the target string
    if my_dict[k] in filedata:
        filedata = filedata.replace(my_dict[k], translated_data_dict[k])

# Write the file out again
with open(output_file, 'w', encoding="utf-8") as file:
    file.write(filedata)
print(translated_data_dict)
#verify!
