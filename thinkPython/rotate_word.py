def rotate_word(s, n):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    new_str = ''

    if n > 13 or n < -13:
        return "Error: number should only be from -13 to 13"

    for c in range(len(s)):
        for l in range(len(alpha)):
            if s[c] == alpha[l]:
                if not l+n > len(alpha) - 1:
                    new_str += alpha[l+n]
                else:
                    new_str += alpha[(l+n)-27]

    return s + " ROT13 is " + new_str

print( rotate_word('melon', 10) )
