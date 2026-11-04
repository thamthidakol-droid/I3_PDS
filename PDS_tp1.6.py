# ---------------------------------------------------------------------------
#Problem 5:Letter Grade 
# --------------------------------------------------------------------------- 
# a          
def letter_grade(score):
    if score < 0 or score > 100:
        return"Invalid"
    elif score >= 97:
        return"A+"
    elif score >= 90:
        return"A"
    elif score >= 80:
        return"B"
    elif score >= 70:
        return"C"
    elif score >= 60:
        return"D"
    else:
        return"F"
list = [99, 90, 85.5, 72, 60, 59.9, 101]
for l in list:
        #print(l, "-->", letter_grade(l))
        print(f"{l:>10} --> {letter_grade(l)}") 
#b
def letter_grade(score):
    if score < 0 or score > 100:
        return"Invalid"
    elif score >=90:
        return"A"
    elif score  >=97:
        return"A+"
    elif score >= 80:
        return"B"
    elif score >= 70:
        return"C"
    elif score >= 60:
        return"D"
    else:
        return"F"
list = [99, 90, 85.5, 72, 60, 59.9, 101]
for l in list:
        #print(l, "-->", letter_grade(l))
        print(f"{l:>10} --> {letter_grade(l)}") 

