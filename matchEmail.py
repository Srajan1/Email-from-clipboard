import pyperclip
import re 
text = str(pyperclip.paste())
phoneREgEx = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
    )''', re.VERBOSE)
mobile = []
tpl = phoneREgEx.findall(text)
mobile = []
for nums in tpl:
    num = str(nums[0]) + str(nums[1])
    mobile.append(num)
ans = ' '.join(mobile)
print(ans)
pyperclip.copy(ans)