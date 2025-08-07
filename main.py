import sys
from stats import get_num_words
from stats import get_char_count
from stats import char_sort

def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
	return file_contents

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	filepath = sys.argv[1]
	text = get_book_text(filepath)
	char_dict = get_char_count(text)

	print(f"""============ BOOKBOT ============
Analyzing book found at {filepath}...
----------- Word Count ----------
Found {get_num_words(text)} total words
--------- Character Count -------""")
	for item in char_sort(char_dict):
		if item["char"].isalpha():
			print(f"{item["char"]}: {item["num"]}")
	print("============= END ===============")

main()
