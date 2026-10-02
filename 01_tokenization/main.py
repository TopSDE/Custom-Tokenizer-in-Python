# tiktoken = Package helps to tokenize and detokenize a text
import tiktoken

enc = tiktoken.encoding_for_model('gpt-4')
text = 'Hey There! My Name is Punith L'
tokens = enc.encode(text)

print("Tokens are:", tokens)

# [19182, 2684, 0, 3092, 4076, 374, 31536, 411, 445]
dec = enc.decode([19182, 2684, 0, 3092, 4076, 374, 31536, 411, 445])
print("Detokens are:", dec)
