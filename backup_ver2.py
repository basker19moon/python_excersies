import os
import time
source = r'C:\Users\Admin\Documents' 
target_dir = r'D:\Documents_Backup2'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)  # Make Directory

today = target_dir+os.sep+time.strftime("%Y%m%d")
now = time.strftime('%H%M%S')
target = today+os.sep+now+'.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print("Successfully created Directory", today)

zip_command = 'Powershell Compress-Archive -Path "{1}" -Destinationpath "{0}"'.format(target, source)
print('zip_command is :')
print(zip_command)
print('Running')
if os.system(zip_command) == 0:
    print("successfully backup to", target)
else:
    print("Backup Failed")