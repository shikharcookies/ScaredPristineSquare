import re
txt = "Lets play cricket"
x = re.search("^Lets.*cricket$", txt)
if x:
  print("Yes! We shall play!")
else:
  print("No we shall not play")