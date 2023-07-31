'''The chapter 4 (PyFilesystem) Challenge:
Get all of the text files in a directory (and it's sub directories)
and add up their file size.  Output the total.'''

from fs.osfs import OSFS

txtFileSize = 0
docxFileSize = 0
rtfFileSize = 0
with OSFS("Exercise Files/PyFilesystem") as myfs:
    for path, info in myfs.walk.info(namespaces=['details']):
        if path.endswith('.txt'):
            txtFileSize += info.size
        elif path.endswith('.docx'):
            docxFileSize += info.size
        elif path.endswith('.rtf'):
            rtfFileSize += info.size

print('Total file sizes for files of type \'X\' are:')
print('\t.txt files:', txtFileSize)
print('\t.docx files:', docxFileSize)
print('\t.rtf files:', rtfFileSize)