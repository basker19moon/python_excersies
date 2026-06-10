poem = '''\
programming is fun
when the work is done
if you wanna make your work also fun:
    use Python!

'''

# Open for writting
f = open('poem.txt', 'w')
# Write text to file
f.write(poem)
# Close the file
f.close()

# If not mode is specified
# 'r'ead mode is assumed by default

f = open('poem.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    # The line already has a newline
    # at the end of each line
    # Since it is reading from the file.
    print(line, end='')
f.close()