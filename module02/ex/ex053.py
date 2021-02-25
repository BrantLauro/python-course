phrase = input('Type a phrase: ').strip().upper().split()
phrase_together = ''.join(phrase)

print(phrase_together[::-1])

if phrase_together == phrase_together[::-1]:
    print('Palindrome')
else:
    print('Not palindrome')