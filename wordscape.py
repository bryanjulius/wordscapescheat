import enchant
import argparse

parser = argparse.ArgumentParser( description='Wordscape cheat sheet!' )
parser.add_argument( '-l', '--letter', metavar='letter' )
parser.add_argument( '-m', '--min', metavar='min' )

ench = enchant.Dict("en_us")

args = parser.parse_args()
letters = args.letter
min = args.min
letters_list  = []
popped_letters = []
words = []
	
def match_ikot( letter, let_list ):
	global words
	for let in range( len( let_list ) ):
		temp_list = let_list.copy()
		new_letter = letter + temp_list.pop( let )
		if( len(new_letter) >= int(min) and ench.check( new_letter ) and words.count( new_letter ) == 0  ):
			words.append( new_letter )
		match_ikot( new_letter, temp_list )
	

for letter in letters:
	letters_list.append( letter )
	match_ikot( "", letters_list )

words.sort()
for word in words:
	print(word)
