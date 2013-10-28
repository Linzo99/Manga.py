#!/usr/bin/env python

import sys
sys.path.append(r'src/')

import mangafox
import mangainn
import mangapanda
import mangastream
import mangareader

def main():
	url = raw_input("Enter the link to the manga\n")

	site_name = url

	if site_name[:7] == 'http://':
		site_name = site_name[7:]

	if site_name[:4] == 'www.':
		site_name = site_name[4:]

	i = 0
	while site_name[i] != '.':
		i += 1

	site_name = site_name[:i]

	if site_name == 'mangareader':
		mangareader.main(url)
	elif site_name == 'mangafox':
		mangafox.main(url)
	elif site_name == 'mangainn':
		mangainn.main(url)
	elif site_name == 'mangapanda':
		mangapanda.main(url)
	elif site_name == 'mangastream' or site_name == 'readms':
		mangastream.main(url)
	else:
		print 'Site not recognised, it\'s not supported yet or the link is not recognised. Please contact the developers.'

if __name__ == '__main__':
	main()