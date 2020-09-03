"""
Play with ANAGRAMS !!
Get n number of words from STDIN, remove all the words that are permutations of any other word
in the given set of inputs. Finally, print the remaining words in ascending order.

Example
-------
Please enter number of Words: 3
world
hello
lhelo
Result = ['hello','world']
"""

from collections import Counter

def anagram( words ):
	for i,word in enumerate(words):
		for j in words[i+1:]:
			if Counter(j) == Counter(word):
				words.remove(j)
	return sorted( words )

if __name__ == '__main__':
	words = []
	for _ in range( int(input('Please enter number of Words: ')) ):
		words.append(input())
	print( anagram(words) )
