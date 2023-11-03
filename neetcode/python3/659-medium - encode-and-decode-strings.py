class Solution:
    """
    https://www.lintcode.com/problem/659/description

    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.

    APPROACH:
    DELIMIT CHAR: ,
    ESCAPE CHAR: \

    , -> \,
    \ -> \\
    \, -> \\\,
    ,\ -> \,\\
    DURING ENCODING
    If encountering an escape char (\) in the string,
        Append an escape char first

    If encountering the delimit char (,) in the string,
        Append an escape char first

    DURING DECODING
    If encountering an escape char (\), 
        If the next char is ',' ... treat , as part of string
        If the next char is '\' ... treat \ as part of string
        If the next char is anything else, something's wrong
    """
    def encode(self, strs):
        # INEFFICIENT STRING CONCATENATION
        output = ""
        
        for index, s in enumerate(strs):
            for c in s:
                if c == ",":
                    output += "\,"
                elif c == "\"":
                    output += "\\"
                else:
                    output += c
            # After entire string, add ","... don't add comma for last string
            if index != len(strs)-1:
                output += ","

        print("ENCODE OUTPUT: ", output)
        
        return output



    """
    @param: str: A string
    @return: decodes a single string to a list of strings

    EXAMPLE ENCODED: 
    ORIG: ["lint", "code", "love", "you"]
    "lint,code,love,you"

    ORIG: ["commas,", "fuc\k", "shit up"]
    "commas\,,fuc\\k,shit up"
    """
    def decode(self, str):
        output = []
        skip = False # Bool to skip char if escape encountered
        curr = ""
        
        for index, c in enumerate(str): 
            if skip:
                skip = False
                pass

            if c == "\"": # next char will be , or \
                curr += str[index+1]
                skip = True
                
            elif c == ",": # end of word -> finish word, append to list, clear curr
                output.append(curr)
                curr = ""

            else: # normal append to new string
                curr += c
        
        output.append(curr) # append last word
        print("DECODE OUTPUT: ", output)
        return output

        # write your code here