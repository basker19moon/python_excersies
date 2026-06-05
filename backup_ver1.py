import os
import time

# 1. Th files and directories to be backup are
# specified in a list
# example on windows
# source = ["'C:\\my Doucuments'"]
# Example on Mac OS X and Linux

source = r'C:\Users\Admin\Documents'

# Notice we have to use double quotes inside a string
# for names with spaces in it. We could have also used
# a raw string by writing [r'c:\my Documents']

# 2. The backup must be stored in a 
# main backup directry 
# example on windows:
# target_dir = ["'D:\Documents_Backup'"] 
# Example on mac os x Linux 

target_dir = r'D:\Documents_Backup'

# Remember to change this to which folder you will be using 

# 3. Ths files are backed up in to a zip file
# 4. The Name of the zip archive is the current date & time

target = target_dir + os.sep+time.strftime('%Y%m%d%H%M%S')+'.zip'
print(target)
# Create target directory if it is not present 
if not os.path.exists(target_dir):
    os.mkdir(target_dir) # Make directory 

# 5. We use the zip command to put the fils in a zip archive

#zip_command =  'zip -r {0} {1}'.format(target, ''.join(source))
zip_command = 'powershell Compress-Archive -Path "{1}" -DestinationPath "{0}"'.format(target, source)

# Run the backup 
print('Zip command is :')
print(zip_command)
print('Running')
if os.system(zip_command) == 0: 
    print('Successful backup to', target)
else:
    print("Backup Failed")