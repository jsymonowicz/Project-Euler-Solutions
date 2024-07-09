"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are  3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out
in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters
The use of "and" when writing out numbers is in compliance with British usage

My program is able to calculate sum of numbers until 21,000
"""

num_words = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
    8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
    14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
    19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
    60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'hundred', 1000: 'thousand'
}

def num_counter(num):
    count = 0
    if i <= 20:
        count = len(num_words[i])
    elif i < 100:
        tens = i // 10 * 10
        units = i % 10
        count = len(num_words[tens])
        if units != 0:
            count += num_word_count[units]
    elif i < 1000:
        hundred = len(num_words[100])
        hundreds_x = i // 100 
        rest = i - (hundreds_x * 100)
        count = (hundred + len(num_words[hundreds_x]))
        if rest != 0:
            count += (3 + num_word_count[rest]) # 3 for 'and'
    elif i < 21000:
        thousand = len(num_words[1000])
        thousand_x = i // 1000
        rest = i - (thousand_x * 1000)
        count = (thousand + len(num_words[thousand_x]))
        if rest != 0:
            count += (3 + num_word_count[rest]) # 3 for 'and'
    else:
        return False
    return count
    
num_word_count = {}
count = 0
chosen_num = 1000

for i in range(1, chosen_num + 1):
    if i >= 21000:
        print('Breaking the count at', i)
        break
    each_count = num_counter(i) 
    num_word_count[i] = each_count
    count += each_count

if chosen_num < 21000:
    print(f"Letters used until {chosen_num}: {count}")
else:
    print(f"Letters used until 21,000: {count}")