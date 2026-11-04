# ---------------------------------------------------------------------------
#Problem 4: Type-Conversion Detective
# ---------------------------------------------------------------------------
#Part A
print(int("7") + 3.5)
print(str(10) * 3)
print(bool(""), bool(" "))
print(int(3.99))
print(float("1e3"))
print(int(True) + float("2.5"))
print(round(2.5), round(3.5))
print(type(10/2))
#PartB
def safe_int(text):                 
    text = text.strip()                      
    if text.lstrip("-").isdigit():       
        return int(text)
    try:                                     
        return int(float(text))
    except ValueError:
        return None

for sample in["42", "-8", "3.9", "abc", ""]:
    print(repr(sample), "->", safe_int(sample))
#PartC
def safe_int(text):                 
    text = text.strip()                     
    if text.lstrip("-").isdigit():      
        return int(text)
    try:                                     
        return int(float(text))
    except ValueError:
        return None
num1 = safe_int(input("Enter the first number:"))
num2 = safe_int(input ("Enter the second number:"))
if num1 is None or num2 is None:
    print("Please enter valid numbers.")
else:
    print("Sum=", num1 + num2)        
