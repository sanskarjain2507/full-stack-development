str=input("enter any string to check palindrome")
j=0
def is_palindrome(str):
    rev=str[::-1]

    if(str==rev):
       print("palindrome\n")
    else:
       print("not palindrome\n")

is_palindrome(str)
