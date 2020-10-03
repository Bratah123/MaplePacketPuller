<h1>Code Documentation:</h1>
 

## Overall Flow of Program <h2>
 ---
 1. Asking user for a file to analyze. ``function = get_func_to_write()``
 
 2. Passing in the ``function`` variable  to function ``analyze_packet_structure()``, returns a string containing packet structure.
 
 3. ``write_func_output()`` writes the given string from ``analyze_packet_structure()``, into an output txt file in FuncOuput DIR
 
 4. ``beautify()`` is then called on the txt file we just wrote in the previous ``write_func_output()``, it strips all "\n" from the txt file and saves into var packet_struct_arr.
 
 5. Loop through the ``packet_struct_arr`` and concat every string in the array into one string variable, making sure to skip any '' characters in the array.
 
 6. ```py
    for i in range(beautified_len): # removes all empty do while() with no decodes inside them
      if beautified_arr[i] == "do:" and beautified_arr[i + 1] == "while()":
          beautified_arr[i] = ''
          beautified_arr[i + 1] = ''
      if beautified_arr[i] == "  do:" and beautified_arr[i + 1] == "  while()":
          beautified_arr[i] = ''
          beautified_arr[i + 1] = ''
   The ``packet_struct_arr`` is an array which stores each line (i.e. ``packet_stuct_arr = ['do', 'while()']``), we loop through each word of this array and every time a ``"do"``    is found in the array we check the next index of the array to see if its a ``"while()"``. If a ``"while()"`` is found right after a ``"do"`` has been encountered, we remove them both from the array.
   

 7. ```py
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
    
