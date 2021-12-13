import pprint

message = 'This is a test message to count how many times each character is repeated in this sentence. Cheers bro.'

count = {}

for char in message:

    count.setdefault(char, 0)

    count[char] += 1

pprint.pprint(count)
