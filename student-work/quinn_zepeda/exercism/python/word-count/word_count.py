from collections import Counter

def word_count(words):
	cnt = Counter()

	for word in words:
		cnt[word] += 1