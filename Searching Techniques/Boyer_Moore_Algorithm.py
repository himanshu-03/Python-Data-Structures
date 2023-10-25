"""Program for Bad Character Heuristic
of Boyer Moore String Matching Algorithm""" 


NO_OF_CHARS = 256

def badCharHeuristic(string, size):
    '''
    The preprocessing function for
    Boyer Moore's bad character heuristic
    '''
    # Initialize all occurrences as -1
    badChar = [-1] * NO_OF_CHARS

    # Fill the actual value of the last occurrence
    for i in range(size):
        badChar[ord(string[i])] = i

    # Return the initialized list
    return badChar

def search(txt, pat):
    '''
    A pattern searching function that uses the Bad Character
    Heuristic of the Boyer Moore Algorithm
    '''
    m = len(pat)
    n = len(txt)

    # Create the bad character list by calling
    # the preprocessing function badCharHeuristic()
    # for the given pattern
    badChar = badCharHeuristic(pat, m)

    # s is the shift of the pattern with respect to the text
    s = 0
    while s <= n - m:
        j = m - 1

        # Keep reducing index j of the pattern while
        # characters of the pattern and text are matching
        # at this shift s
        while j >= 0 and pat[j] == txt[s + j]:
            j -= 1

        # If the pattern is present at the current shift,
        # then index j will become -1 after the above loop
        if j < 0:
            print("Pattern occurs at shift =", s)

            ''' 
                Shift the pattern so that the next character in the text
                aligns with the last occurrence of it in the pattern.
                The condition s+m < n is necessary for the case when
                the pattern occurs at the end of the text
            '''
            s += (m - badChar[ord(txt[s + m])] if s + m < n else 1)
        else:
            '''
            Shift the pattern so that the bad character in the text
            aligns with the last occurrence of it in the pattern. The
            max function is used to make sure that we get a positive
            shift. We may get a negative shift if the last occurrence
            of the bad character in the pattern is on the right side of the
            current character.
            '''
            s += max(1, j - badChar[ord(txt[s + j])])

while True:
    txt = input('Enter the text (or press Enter to exit): ')
    if not txt:
        break
    pat = input('Enter the pattern to search for: ')
    search(txt, pat)
