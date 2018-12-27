
# All sorted lowercase letters are ahead of uppercase letters.
# All sorted uppercase letters are ahead of digits.
# All sorted odd digits are ahead of sorted even digits.

# lowercase=1
# uppercase=2
# odd=3
# even=4

s=list("Sorting1234")
# s=list("1qaz2wsx3edc4rfv5tgb6yhn7ujm8ik9ol0pQWERTYUIOPASDFGHJKLZXCVBNM")
x_digit=[int(n) for n in s if n.isdigit()==True]
x_char=[n for n in s if n.isalpha()==True]
x_digit = sorted(sorted(x_digit),key=lambda x: 1 if x % 2==0 else 0)
x_digit=list(map(str,x_digit))
print(x_digit)
x_char = sorted(sorted(x_char),key=lambda x: 1 if x.isupper()  else 0)
print(x_char)
s=x_char+x_digit
print(''.join(s))
