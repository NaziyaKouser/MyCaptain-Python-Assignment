file_name=input('Enter filename:')
file=file_name.split('.')
ext=file[-1]
file_type={'py':'Python','txt':'Text','Doc':'Document'}
if ext in file_type.keys():
           print('The extension of the file is',file_type[ext])
