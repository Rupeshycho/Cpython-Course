#Strings are immutable
a='rupesh'
print(len(a))
print(a.upper())
print(a.lower())
print(a.capitalize())
print(a.lower())

b="Rupesh!!!!!!Rupesh rupesh !"
print(b.rstrip("!"))
print(b.replace("Rupesh","AnjuRupesh").rstrip("!"))

splitstr="Rupeshyadav"
print(splitstr.split(" "))

caplitalize="Introduction to js"
print(caplitalize.capitalize())

str1="Welcome to the console"
print(str1.center(50,"="))
print(len(str1.center(50,"=")))
print(len(str1))

print(str1.count("o")) #count finds repeatition 

print(str1.endswith("console"))

str2="welcome to the console"
print(str2.endswith("to", 4, 10))

print(str2.find("the"))  #11: index of first occurence 

# print(str2.index("adfa"))

str3="welcometotheconsole"
print(str3.isalnum())

str4="welcome"
print(str4.isalpha()) #True

str4="welcome00"
print(str4.isalpha()) #False

str5="welcome00"
print(str4.islower())   #True
print(str5.isprintable()) #True
print("\n")
str6="welcome to the jungle\n"
print(str6.isprintable()) #False

str="    "
print(str.isspace())

str1="World Health Organization"
print(str1.istitle())

str7="To kill a mocking bird "
print(str7.istitle()) #false

str9="ISUPPERTRUEWHENALLAREINUPPERCASE"
print(str9.isupper())

str10="!!hello world "
print(str10.startswith("!"))

str11="uppercase"
print(str11.swapcase())


title="rupesh is the great developer with 17lacs per annum"
print(title.title())

title2="his name is Dan. dan is an honest man."
print(title2.title())

