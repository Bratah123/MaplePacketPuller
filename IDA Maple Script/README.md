
# Code Documentation:
 

## Overall Flow of Program:
 1. Asking user for a file to analyze. `function = get_func_to_write()`
 
 2. Passing in the `function` variable  to function `analyze_packet_structure()`, returns a string containing packet structure.
 
 3. `write_func_output()` writes the given string from `analyze_packet_structure()`, into an output txt file in FuncOuput DIR
 
 4. `beautify()` is then called on the txt file we just wrote in the previous `write_func_output()`, it strips all "\n" from the txt file and saves into var packet_struct_arr.
 
 5. Loop through the `packet_struct_arr` and concat every string in the array into one string variable, making sure to skip any '' characters in the array.
 
 6. We split the new ouput given from step 5 into an array named `beautifed_arr`, `write_output.split("\n")`
 
    ```py
    for i in range(beautified_len): # removes all empty do while() with no decodes inside them
      if beautified_arr[i] == "do:" and beautified_arr[i + 1] == "while()":
          beautified_arr[i] = ''
          beautified_arr[i + 1] = ''
      if beautified_arr[i] == "  do:" and beautified_arr[i + 1] == "  while()":
          beautified_arr[i] = ''
          beautified_arr[i + 1] = ''
    ```
    
  7. The `beautifed_arr` is an array which stores each line (i.e. `beautifed_arr = ['do', 'while()']`), we loop through each word of this array and every time a `"do"` is found   in the array we check the next index of the array to see if its a `"while()"`. If a `"while()"` is found right after a `"do"` has been encountered, we remove them both from     the array.
  
   ```py
    for i in range(beautified_len): # checking for any contents inside a do while loop and spacing them out for visual aesthetics
     if beautified_arr[i] == "do:":
         j = i + 1
         while beautified_arr[j] != "while()":
             beautified_arr[j] = f"  {beautified_arr[j]}"
             j += 1
     # some functions, this will cause an index out of range error (comment out this part if so)
     try:
         if beautified_arr[i] == "  do:":
             j = i + 1
             while beautified_arr[j] != "  while()":
                 beautified_arr[j] = f"   {beautified_arr[j]}"
                 j += 1
     except Exception as e:
         print("Some error occured, but it shouldn't affect the decodes() just has to do with aesthetics")
   ```
 8. Similar to step 6 of this program, we loop through each word of the `beautifed_arr[]` array, this time we check the contents of a do while loop. Given an array like   `beautifed_arr = ['do', 'CInPacket::Decode4', 'while()]` we can loop til we hit a `"do"`, once a `"do"` has been found we loop through every word of the array starting    from that `"do"` til we hit a `"while()"` indenting every "decode()" function we find between them.

  9. Finally, we concat every word in `beautifed_arr` (after cleaning from prev steps) array into variable = `clean_output`.
  
  10. `print()` and `write_func_output()` with the final variable `clean_output` as argument.
---
## Methods:
- `def print_dbg(msg)`
	- References:  9 
	- Location of references:
		- `check_keyword_and_print(word)`: 2
		- `analyze_packet_structure(function)` : 7
	- Prints out a given string, if `PRINT` constant is `True` (see line 11).
		| Parameter | Type | Description |
		| --- | --- | --- |
		|   msg | string | message to print |
		
		Returns: `void`
	---
- `def print_dbg(msg)`
	- References:  9 
	- Location of references:
		- `check_keyword_and_print(word)`: 2
		- `analyze_packet_structure(function)` : 7
	- Prints out a given string, if `PRINT` constant is `True` (see line 11).
		|  | Parameter | Type | Description |
		| --- | --- | --- |
		|   msg | string | message to print |
		
		Returns: `void`
	---
- `def check_keyword_and_print(word)`
	- References:  1 
	- Location of references:
		- `analyze_packet_structure(function)` : 1
	- Given a word, check if that word is a "decode" function and print out a corresponding string in `KEYWORD_PRINT` array.
		|  | Parameter | Type | Description |
		| --- | --- | --- |
		|   word | string | word to check and print if `True` |
		
		Returns: `boolean`
	---
- `def print_dbg(msg)`
	- References:  9 
	- Location of references:
		- `check_keyword_and_print(word)`: 2
		- `analyze_packet_structure(function)` : 7
	- Prints out a given string, if `PRINT` constant is `True` (see line 11).
		|  | Parameter | Type | Description |
		| --- | --- | --- |
		|   msg | string | message to print |
		
		Returns: `void`
	---
- `def check_keyword_and_print(word)`
	- References:  1 
	- Location of references:
		- `analyze_packet_structure(function)` : 1
	- Given a word, check if that word is a "decode" function and print out a corresponding string in `KEYWORD_PRINT` array.
		|  | Parameter | Type | Description |
		| --- | --- | --- |
		|   word | string | word to check and print if `True` |
		
		Returns: `boolean`
	---
- `def check_keyword_and_return(word)`
	- References:  3 
	- Location of references:
		- `analyze_packet_structure(function)` : 3
	- `check_keyword_and_return(word)` extends `def check_keyword_and_print(word)`  in functionality but returns the corresponding string in `KEYWORD_PRINT` array instead of printing to console.
		|  | Parameter | Type | Description |
		| --- | --- | --- |
		|   word | string | word to check and return if `True` |
		
		Returns: `string`
	---
- `def get_func_name(txt_file_name)`
	- References:  1 
	- Location of references:
		- `analyze_packet_structure(function)` : 1
	- Opens a file in `Functions` directory with the given file name and returns the first line of the txt file (which is the function name) then closes the file.
		|  | Parameter | Type | Description |
		| --- | --- | --- |
		|   txt_file_name | string | text file name to open in `Functions` DIR |
		
		Returns: `string`
	---
- `def add_decode_to_list([list], word)`
	- References:  1 
	- Location of references:
		- `analyze_packet_structure(function)` : 1
	- Given a `list` and a `word` (function name) check if that word is a `"decode"` function, and if it is add it to the given list.
		|  | Parameter | Type | Description |
		| --- | --- | --- |
		|   list | `string[]` | list to append the function to |
		|   word | string | word to check if its a decode and to add to list |
		
		Returns: `string`
	---
- `def beautify(file_name)`
	- References:  1 
	- Location of references:
		- `__main__` : 1
	- Open a file with the given file name and remove every `newline` (`'\n'`) and adds it to an array.
		|  | Parameter | Type | Description |
		| --- | --- | --- |
		|   file_name | string | text file to open |
		
		Returns: `string[]`
