# File objects - code snippets
with open('test.txt', 'r') as file:
    contents = file.read()
    print(contents) # good for small file.

# better way of reading for a Large file. Not loading the whole file in memory.
with open('large.txt', 'r') as f:
    f_contents = f.readlines()
    print(f_contents) # prints a list of all the new lines.

with open('large.txt', 'r') as f:
    for line in f:
        print(line, end='')
        # read file line by line rather than all at once. iterate over the lines in a file and print 'em
        # no memory issues


# # more control over exactly what to read from the file. print file in small chuncks of characters
with open('large.txt', 'r') as f:
    chars_to_read = 15
    f_contents = f.read(chars_to_read) # arg n of characters to read
    while len(f_contents) > 0:
        print(f_contents, end='')
        print(f.tell())
        f_contents = f.read(chars_to_read)

#  Writing to files - making a copy of a file.
with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)
#
# make copy an image file. Reading and writing bytes - not chars (Binary mode)
with open('sava.jpg', 'rb') as ri:
    with open('sava2.jpg', 'wb') as wi:
        for line in ri:
            wi.write(line)

# # set a chunk size to read
with open('sava.jpg', 'rb') as ri:
    with open('sava2.jpg', 'wb') as wi:
        chunk_size = 4096
        ri_chunk = ri.read(chunk_size) # size of data to read and then write at each iteration
        while len(ri_chunk) > 0:
            wi.write(ri_chunk)
            ri_chunk = ri.read(chunk_size)
