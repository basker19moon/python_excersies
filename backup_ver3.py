import os
import time
source = r'C:\Users\Admin\Documents'
target_dir = r'D:\Documents_Backup3'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today = target_dir+os.sep+time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

comment = input("Please Enter a comment --> ")

if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'

if not os.path.exists(target):
    os.mkdir(today)
    print("Successfull Created Directory", today)

zip_command = 'Powershell Compress-Archive -Path "{1}" -Destinationpath "{0}"'.format(target, ''.join(source))

print('zip_command is: ')
print(zip_command)
print("Running...: ")

if os.system(zip_command) == 0:
    print("Successfully Backedup to ", target)
else:
    print("Backup Failed..!")
