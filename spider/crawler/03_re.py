# -*- coding:utf8   -*-
# @Author :George华
# @Time : 2020/6/15 2:37 下午

import re

pat = re.compile("AA", re.IGNORECASE)
m = re.search("bc", "abcaa")
print(m)
