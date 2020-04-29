# Anil Kumar Ravuru

import os

file_names = os.listdir()
mpg_files = sorted(list(filter(lambda x: '.mpg' in x, file_names)))
cmd = 'cat '+' '.join(mpg_files)+'> final_movie.mpg'
os.system(cmd)
cmd = 'rm -f '+' '.join(mpg_files)
os.system(cmd)
