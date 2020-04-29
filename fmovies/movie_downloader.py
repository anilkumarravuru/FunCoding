# Anil Kumar Ravuru


# Sequential Download

"""
import os
from multiprocessing import Pool

def download_movie(cmnd):
	template_string = ".ts' -H"
	pos = cmnd.index(template_string)
	timer = 10
	while(True):
		timer_string = format(timer, '4d').replace(' ','0')
		pre_cmnd = cmnd[:pos-4]+timer_string+cmnd[pos:]+' > '+str(timer)+'.mpg'
		print(pre_cmnd[pos-4:pos])
		os.system(pre_cmnd)
		if os.stat(str(timer)+'.mpg').st_size < 10**4:
			print('Failed ', str(timer))
			return
		print('Downloaded ', str(timer), '.mpg')
		timer += 1

url = "curl 'https://bxday.mcloud.to/38/12c3522a626cd2c9/4ebf972c59e5acff2937f41504746bb5cbf9a1b54c4cbda439a6559acd118790ac28a1447fd5d36c9ae0c502a1cb6ae46beb0ff38b7d269f66cafc910bdd236ea3f5c1ea1449ad88946f59db3a8d68e3e57231dac00a10714ba0ac5d209f92d77ef47d2e314317e98bb34129d95a8e22/hls/720/720-0010.ts' -H 'authority: bxday.mcloud.to' -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36' -H 'sec-fetch-dest: empty' -H 'accept: */*' -H 'origin: https://mcloud.to' -H 'sec-fetch-site: same-site' -H 'sec-fetch-mode: cors' -H 'referer: https://mcloud.to/embed/vq97j4?key=47ce7b2bb6d7f522e952ceae1adc0330&sub.file=https%253A%252F%252Fstaticf.akacdn.ru%252Ff%252Fsubtitle%252F32127.vtt%253Fv1' -H 'accept-language: en-GB,en-US;q=0.9,en;q=0.8' -H 'cookie: _ga=GA1.2.857792058.1584730416; _gid=GA1.2.255087722.1584730416; _gat=1' --compressed"
download_movie(url)
"""



# Parallel download
import os
from multiprocessing import Pool

def download_movie_parallel(part_number):
	global url
	template_string = ".ts' -H"
	pos = url.index(template_string)
	os.system(url[:pos-4]+part_number+url[pos:]+' > '+part_number+'.mpg')

url = "curl 'https://fxykx.mcloud.to/3/1e6581062f89d2fe/4b14c0971d20750cf9e36dbc06522a44a9c8c33f17ee8956247d6388762cb03cfe54df560f357f5edcfbc76d8a2be924831fdb6d338700adc4b1296c12bed5dcba67f0c01ef8fe2c59d9f316374d9b27ed29726d1288629c65c644401e8351d0/hls/720/720-0006.ts' -H 'authority: fxykx.mcloud.to' -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36' -H 'sec-fetch-dest: empty' -H 'accept: */*' -H 'origin: https://mcloud.to' -H 'sec-fetch-site: same-site' -H 'sec-fetch-mode: cors' -H 'referer: https://mcloud.to/embed/wqo0x4?key=1b5140c71a9d985710f9c9afa95633d5&sub.file=https%253A%252F%252Fstaticf.akacdn.ru%252Ff%252Fsubtitle%252F37801.vtt%253Fv1' -H 'accept-language: en-US,en;q=0.9' -H 'cookie: __cf_bm=35b2f71137d922f71e64a52206b2b9fc7b582e82-1587515735-1800-AYF66qFBPzdMeSzxPBBnYt9O8iVnJd6nU64O5behsPjjhliDKugZpX6kncpgUE8guBWVGUEbIJu23QYrOQcm56NSuQyzoS8eQ9T1gg4oiSY+' --compressed"
times = [format(_, '4d').replace(' ','0') for _ in range(1, 1127)]
p = Pool(16)
p.map(download_movie_parallel, times)
