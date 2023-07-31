# Python Essential Libraries by Joe Marini course example
# Example file for using PyFilesystem

# import the PyFilesystem library
from fs.osfs import OSFS
from fs.zipfs import ZipFS

# TODO: open a local filesystem for the current directory
# home_fs = OSFS("~/")
# myShit = home_fs.listdir('/Desktop')
# print(myShit)
# with OSFS('Exercise Files/PyFilesystem') as myfs:
#     if (not myfs.exists('testdir')):
#         myfs.makedir('testdir')
#     with myfs.open('testdir/samplefile.txt', mode='w') as f:
#         f.write('This is some horse shit!')
#     with myfs.open('testdir/samplefile.txt', mode='a') as f:
#         f.write('\nWhat happens this time?')
#         f.write('\nAre we having fun yet?')
#     with myfs.open('testdir/samplefile.txt') as f:
#         content = f.read()
#         print(content)

#     info = myfs.getinfo('testdir/samplefile.txt', namespaces=['details','access'])
#     print('Name:', info.name)
#     # print(info.is_dir)
#     print('Size:', info.size)
#     print('Type:', info.type)
#     print(info.modified)
#     print(info.group)

# TODO: try opening and reading a ZIP archive
with ZipFS('Exercise Files/PyFilesystem/FileExamples.zip') as thezip:
    if(thezip.exists('FileExamples/File1.txt')):
        with thezip.open('FileExamples/File1.txt') as f:
            content = f.read()
            print(content)

