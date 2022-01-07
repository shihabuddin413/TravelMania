
my_icons=[
'list.svg',
'pencil-square.svg',
'bar-chart-line-fill.svg',
'upload.svg',
'file-earmark-medical.svg',
'plus.svg',
'facebook.svg',
'twitter.svg',
'mailbox.svg',
'instagram.svg',
'share.svg'
]


import os
import glob 

os.chdir("./icons/")
all_files =  glob.glob("*.svg")
print(f'number of files {len(all_files)}')

counter =0
for i in all_files:
	if (i in my_icons):
		print(f"\nWe will not delete {i}")
	else:
		os.system(f"ERASE {i}")
		print(f"{counter} ", end="")
	counter +=1