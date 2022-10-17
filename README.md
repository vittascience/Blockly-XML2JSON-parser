# XML to JSON and vice-versa for strings of interest processing

**A simple Python parser for XML to JSON transcription**

The script was written & intially designed for automating the translation of Blockly XML blocks. 
***parser.py*** provides the following functionalities:
- Given an original XML formated file containing block strings ***original.js***. The file is parsed for strings of interest. These SoF are then formatted in a JSON format initially designed for G Translate API compatibility. 
- The intermediary JSON file ***temp.json*** is generated. Once ***temp.json*** is processed into ***processed.json***,  the inverse operation is proceeded by converting the processed file into XML formatting for Blockly. 
- The output file ***output.js*** then contains the processed strings of interest.
