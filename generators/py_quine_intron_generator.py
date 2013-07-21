s = """print "source_code = " + str(source_code)\nintron=""\nprint ''.join([chr(x) for x in source_code]),""" # These are the lines that will be printed after the list 
print "source_code = " + str([ord(x) for x in s]) # Then print the list of chars which represent the message above
print s # Print the quine
