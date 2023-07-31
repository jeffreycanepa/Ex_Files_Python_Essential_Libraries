# Python Essential Libraries by Joe Marini course example
# Example file for using PyFilesystem directory functions
from fs.osfs import OSFS

# TODO: print a directory tree listing
# with OSFS('Exercise Files/PyFilesystem') as myfs:
#     myfs.tree()

# TODO: use directory operation functions
# with OSFS('Exercise Files/PyFilesystem') as myfs:
'''Get list of items in folder FileExamples''' 
    # dirList = myfs.listdir('FileExamples')
'''Print out the list of items'''
    # print(dirList)
'''Sort the list of items then print'''
    # print(sorted(dirList))

'''After adding File4.py, filter dirList to only get files that are of type .txt'''
    # dirList = list(myfs.filterdir('FileExamples',files=['*.txt']))
    # print(dirList)

# TODO: Use resource info with scandir
# with OSFS('Exercise Files/PyFilesystem') as myfs:
#     dirlist = myfs.scandir('FileExamples', namespaces=['details'])
#     for info in dirlist:
#         print(info.name, info.size)
    
# TODO: make a copy of a directory
# with OSFS('Exercise Files/PyFilesystem') as myfs:
#    myfs.copydir('FileExamples', 'CopyOfFileExamples', create=True)


# TODO: remove a directory
with OSFS('Exercise Files/PyFilesystem') as myfs:
   if(myfs.exists('CopyOfFileExamples')):
      myfs.removetree('CopyOfFileExamples')