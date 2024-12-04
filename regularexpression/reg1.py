# text="fatcatrunsurveyfasttocaththerat"
from re import finditer

text="fatcatrunsurveyfasttocaththerat"

matcher=finditer("(at)",text)

for obj in matcher:
    print(obj.groups())
    print(obj.start(),obj.group())



