#!/usr/bin/env python2

import sys
import json
import gkeepapi

keep = gkeepapi.Keep()
keep.login('GOOGLEUSERNAME','APPPASSWORD')

data = json.load(sys.stdin)

for i in range(len(data)):
  for key in sorted(data[i].keys()):
    if "title" in key:
      ListTitle=str(data[i]["title"])
      KeepLists=keep.find(query=ListTitle)

      if not any(KeepLists):
       print("Create key ",ListTitle)
       glist = keep.createList(ListTitle)

       for x in data[i]["tasks"]:
         ListItem=str(x["title"])
         print("List Item ",ListItem)
         TaskComplete=False
         if x["completed"] == 1:
             TaskComplete=True
         glist.add(ListItem,TaskComplete)

      else:
          print("List exists: ", ListTitle)

keep.sync()
