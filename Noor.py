import os,platform
bit = platform.architecture()[0]
if bit == '64bit':
  from Noor import Main
	Main()
elif bit == '32bit':
	from Noor32 import Main
  Main()
else:
	print('\n soory your device not support this tool');exit()
