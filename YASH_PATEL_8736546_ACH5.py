import re

source ="Lorem ipsum doflor szit ametß, consqecytetu$r adipibsching elit, yash sed do eiusmod patel tewmporα incid6kgidunt ut labq8ore et café 8736546 dolore_ magna aliqua. Purus! sit{|}~ \t\n\r\x0b\x0c amet volutpat cons&jequat mau7ris. Penaxtibus et"

Alleffs = re.findall("y", source)
print("number of characters as per letter y: ",len(Alleffs))

AllDigits = re.findall("\d", source)
print("number of digits found: ", len(AllDigits))

AllAlphaNumerics = re.findall("\w", source)
print("number of Alpha numerics characters found: ", len(AllAlphaNumerics))

AllNonAlphaNumerics = re.findall("\W", source)
print("number of non-alpha numerics characters found: ", len(AllNonAlphaNumerics))

AllSpaces = re.findall("\s", source)
print("number of spaces found:",len(AllSpaces))
