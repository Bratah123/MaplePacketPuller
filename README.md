# Maplestory Packet Puller

Features:
 - Pulls Keywords in IDA Pseudocode and formats them in order for Server Encodes
 - Options to turn on in order to have a higher accuracy while pulling packet structures
 - Lets you see the structure of a packet
 - Writes all packet structures to an output file (FuncOutput)
 
Some things need to know / Issues:
  - Edge case functions may cause error, see comments in code to fix it in this case (line 159)
  - while() loops aren't handled to let you see whether a decode is in the scope of one well (can be rectify if GET_ALL_DECODES = true maybe)
  - GET_ALL_DECODES constant in the code, when turned to true has a higher accuracy for finding decodes but at the price of aesthetics :P
  - This script is assuming you have named the decodes function in IDA accordingly to your function you want to pull packet structure from
  - Does not display switch cases (can figure out yourself), can be easily handled 

Tech Stack Used
 - Python Version 3.8.6
 - IDA 7.0 Pro 32-bit (for analyzing an unpacked Maplestory.exe)
 - Atom Text Editor

<h1> How to use</h1>
 0.5) You will have to create a new txt file in the Functions Directory with the copy pasted code from IDA (examples in there)
 
 1. Open it in a text editor of choice (I use atom), open cmd and type in Analysis.py
 
 2. Just type the name of the file you want to analyze (the txt file you just created)
 
 3. Let the program analyze it.
 
 4. Now packet structure should be yours!
  

 It should look like this:
 ![OnSetField](https://media.discordapp.net/attachments/746519006961336370/755117561024086036/061591b5c3d0f4a3247f9367b91b9843.png)
