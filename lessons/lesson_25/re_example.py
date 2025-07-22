text = '''Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth.'''

text.startswith('Tom')
text.endswith('n wealth.')

'Tom' in text

text.count('Tom')

# (20 or 200 or 200) + 0-2 words + (USD or usd)
pattern_usd = r'\b[\d]{2,4}\b\s([A-Za-z]+\s){0,2}(usd|USD)'
text_usd = '''
bla-bla 250 USD
bla-bla 250 of usd

bla-bla 25000 USD
bla-bla 250 of EUR
bla-bla 250 of the a usd
'''

patter_phone = r'\(0[\d]{2}\)\s[\d]{3}(-[\d]{2}){2}'

text_phone = '''
(096) 555-55-55
(096) 555-55-5
(196) 555-55-55'''

import re


is_usd_in_text = re.findall(pattern_usd, text_usd)
assert is_usd_in_text, f'Cant find {pattern_usd} in text:\n{text_usd}'

searched_data = re.finditer(pattern_usd, text_usd)
for t in searched_data:
    print(t.group(0))


# css selector
# div.RNNXgb div span
# xpath
# //div[@class="RNNXgb"]//div//span

# div.RNNXgb > div
# //div[@class="RNNXgb"]/div

# #gb
# *[@id="gb"]

# /html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[1]/div[2]