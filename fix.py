import os
for root, _, files in os.walk('.'):
  for f in files:
    if '?' in f:
      print f
      src = os.path.join(root, f)
      dst = os.path.join(root, f.split('?')[0])
      os.rename(src, dst)
