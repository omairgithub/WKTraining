str="How are you guys"
#len is used to find length of the string
print(len(str))
#[a:b] returns words from ath index to (b-1)th index of string
#if a&b<0 then it will traverse indexes from last word of string

print(str[1:4])
#[a:b:c] returns words from ath index to (b-1)th index of string leaving c no. of characters of string
print(str[1:10:2])
print(str.endswith("guys"))
# count() counts the no. of occurrences of a given character/word
print(str.count("o"))
# capitalize capitalize 1st letter of string
print(str.capitalize())
# replace one word/character by other word/character
print(str.replace("o","a"))
# upper() capitalize the whole string
print(str.upper())