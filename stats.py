def get_num_words(texts):
        count = 0
        for text in texts.split():
                count += 1
        return count

def get_char_count(texts):
	count = {}
	for char in texts.lower():
		if char not in count:
			count[char] = 1
		else:
			count[char] += 1
	return count

def sort_on(items):
	return items["num"]

def char_sort(chars):
	sort_list = []
	for char in chars:
		sort_list.append({"char": char, "num": chars[char]})
	sort_list.sort(reverse=True, key=sort_on)
	return sort_list
