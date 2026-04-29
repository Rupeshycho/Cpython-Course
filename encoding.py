import encoding
import decodestring()
encoded = "Rupesh".encode("ASCII")
print(encoded)



#input
encod=input("Enter the string: ")
print(encod.encode("ASCII"))


text="Hello Rupesh"
encoded = text.encode("UTF-8")
print("Encode: \n",encoded)

decoded = encoded.decode("UTF-8")
print("Decode: \n", decoded)
