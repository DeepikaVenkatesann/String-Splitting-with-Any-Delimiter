# Custom-Splitting-with-Any-Delimiter

The customsplit function is a  function that splits a given input string into different fields using custom delimiters.

This can be useful when you have specific delimiters in mind that are not covered by the built-in string splitting functions.

## Explanation
This line defines a function named customsplit that takes two parameters:
inputstring (the string to be split) and delimiters (a list of delimiters to use for splitting).

map(re.escape, custom_delimiters): function to each element in the custom_delimiters list. re.escape() escapes any special characters.

' '.join(): This joins the escaped delimiters using a space as a separator. 

re.split(): This splits the inputstring using the regular expression created from the escaped delimiters. 

filter(None, ): This filters out empty strings from the list of substrings using the filter() function. 
The None function serves as the filter condition, effectively removing empty strings from the list.

list(): This converts the filtered result into a list.
### Function Signature

python
def custom_split(input_string, delimiters):

    Splits the inputstring into fields using the specified delimiters.

    Parameters:
    - inputstring (str): The input string to be split.
    - delimiters (list): A list of delimiters used for splitting.

    Returns:
    - list: A list of split fields.
## Example Output
Input:'sdfkdjsadfsd diweiw; 1231:foo'
Delimiters [' ', ';', ':'], 
Output :['sdfkdjsadfsd', 'diweiw', '1231', 'foo']

