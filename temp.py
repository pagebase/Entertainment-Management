import re

patt=r"(\d+\.)"
with open("TV_Shows.md", "r") as file:
    text=file.read()
data=re.findall(patt, text)
# print(len(data))
data1=re.sub(r"[^0-9]", '',str(data[36]))
print(data1)
# print(len(data1[1]))
# print(data1[63])
# sr_number=int(data1[len(data1-2)+data1[len(data-1)]])
# print(sr_number)