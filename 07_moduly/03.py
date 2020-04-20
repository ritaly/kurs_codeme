import file_helper as fh

txt = fh.safe_open('nadwaga.txt')
print(txt)

txt_to_save = 'nananannana \t oooooo\nnowy napis'

fh.safe_save('new_file.txt', txt_to_save)