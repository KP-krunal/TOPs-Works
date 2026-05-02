# Write a program to check all list elements are alphabetics or not.
# E.g ["ewr","wewe","123"] output False 
# ["asd","wer","qqq","ddd"] output True

lst_strings = ["asd", "wer", "qqq", "ddd"]
lst_strings2 = ["ewr", "wewe", "123"]

for string in lst_strings:
    if not string.isalpha():
        print("False")
        break
else:    
    print("True")

for string in lst_strings2:
    if not string.isalpha():
        print("False")
        break
else:    
    print("True")