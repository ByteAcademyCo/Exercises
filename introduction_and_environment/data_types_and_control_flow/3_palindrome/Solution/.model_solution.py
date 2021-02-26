word = input()
is_palindrome = True
for i in range(len(word)//2):
    if not word[i] == word[len(word)-i-1]:
        is_palindrome = False
        break