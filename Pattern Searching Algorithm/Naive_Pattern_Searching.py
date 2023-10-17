# Python3 program for Naive Pattern
# Searching algorithm


def search(pat, txt):
	M = len(pat)
	N = len(txt)

	# A loop to slide pat[] one by one */
	for i in range(N - M + 1):
		j = 0

		# For current index i, check
		# for pattern match */
		while(j < M):
			if (txt[i + j] != pat[j]):
				break
			j += 1
   
		if (j == M):
			print("Pattern found at index ", i)


# Driver's Code
if __name__ == '__main__':
	txt = "AABAACAADAABAAABAA"
	pat = "AABA"
	
	# Function call
	print('Below iis an` example of Naive Pattern Searching Algorithm\n')
	print('It is being implemented for the following text and pattern: \n')
	print('	Text = "AABAACAADAABAAABAA" pattern = "AABA"')
 
	search(pat, txt)
    #try it yourself
	print('\nNow try it yourself\n')
	txt = input("Enter the text: ")
	pat = input("Enter the pattern: ")
	search(pat, txt)