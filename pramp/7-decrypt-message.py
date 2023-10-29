"""
Encryption
convert every letter to ascii
add 1 to first letter
  all others, add value of prev letter
subtract 26 from each letter until in range of lowercase 'a-z'

decrypted message: z
step 1: 122
step 2: 96
step 3: 96
enc m:  a

Decrypted message:	c	r	i	m	e
Step 1:	99	114	105	109	101
Step 2:	100	214	319	428	529
mult 26:0   4   
Diff:   0   104 208 312 416
Step 3:	100	110	111	116	113
ascii: 100 110 11
Encrypted message:	d	n	o	t	q

First char: 
increment first char

Other chars:
convert to ascii value
add 26 until new val == 
subtract value of next letter

input:  word = "flgxswdliefy"
f   l   g   x
102 108 103
-1  -102
101 +26*4
    110
e   n

enc[n] = dec[n] + secondStep[n-1] + 26m


output: "encyclopedia"

"""
"""
REVIEWING PROBLEM July 14

ENCRYPT STEPS:
1. convert to int
2. add 1 / add val of prev letter
3. subtract 26 until in range
4. convert to ascii

DECRYPT STEPS:
1. convert to int
2. subtract 1 / subtract prev letter (second step)
3. add 26 until in range
4. convert to ascii

input:  word = "flgxswdliefy"
f   l     g       x
102 108   103     120
-1  -102  -108    -103
101 +26*4 +26*4   +26
    110   99
e   n     c

enc[n] = dec[n] + secondStep[n-1] + 26m


output: "encyclopedia"



"""

def decrypt(word):
  # enc[n] = dec[n] + secondStep[n-1] + 26m
  # DO ALGEBRA TO SOLVE FOR DEC[n]
  # dec[n] = enc[n] - secondStep[n-1] + 26m 
  # chr()
  # ord() 
  
  result = ""
  
  """
  d     n     o     t     q
  100   110   111   116   113
  -1    -100  -110  -111  -116
  99    10+26 1+26  5+26  -3+26
  99    114   105   109   101
  c     r     i     m     e
  """
  
  # first char
  enc_first = ord(word[0])
  val = enc_first - 1
  dec_first = chr(val)
  result += dec_first

  # Save previous char
  prev_enc_val = enc_first
  
  for c in range(1,len(word)):
    val = ord(word[c])
    val = val - prev_enc_val
    prev_enc_val = val # update prev_enc_val right after using it
    while val < 97:
      val += 26
    dec_char = chr(val)
    result += dec_char
  
  return result
    
word = "dnotq"
print(decrypt(word))
# test = decrypt(word) == "crews"
# print("PASS" if test else "FAIL")

word = "flgxswdliefy"
print(decrypt(word))
# test = decrypt(word) == "encyclopedia"
# print("PASS" if test else "FAIL")