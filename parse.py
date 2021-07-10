# -*- coding: utf-8 -*-
"""

"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

__author__ = 'timmyliang'
__email__ = '820472580@qq.com'
__date__ = '2021-07-11 00:45:13'


import json
import os

input_path = r"F:\repo\TimmyPKM\Plugins\HCHaase\TOCgeneric\plugin.info"

DIR = os.path.dirname(input_path)
json_path = os.path.join(DIR,"data.json")
# data_path = os.path.join(DIR,"data")
with open(input_path,'r',encoding="utf-8") as f:
    data = json.load(f)

data.update(json.loads(data.pop("text","")))
with open(input_path,'w') as f:
    json.dump(data,f,indent=4)
     

