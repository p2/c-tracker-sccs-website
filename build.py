#!/usr/bin/env python3
#
#  Uses HTML data from c-tracker-content and renders them, using Jinja2, into CTracker/HTMLContent/
#
#  Requirements:
#  - jinja2
#  - markdown

import io
import os.path
import markdown
from jinja2 import Environment, PackageLoader


env = Environment(loader=PackageLoader(__name__, 'templates'))
_template = env.get_template('base.html')
_source = 'c-tracker-sccs-content'
_target = '.'
_languages = ['en', 'de', 'fr']
_files = ['index.html', 'team.md']


# run all files in all languages
def run():
	for file in _files:
		run_file(file)

# run one file in all languages
def run_file(file):
	print('-->  Building file {}'.format(file))
	for lang in _languages:
		langdir = '{}.lproj'.format(lang)
		if not os.path.exists(os.path.join(_source, langdir, file)):
			print('===>  Does not exist in {}, trying English'.format(lang))
			langdir = 'en.lproj'
			if not os.path.exists(os.path.join(_source, langdir, file)):
				print('xxx>  Not available in English, skipping')
				continue
		run_file_in_lang(langdir, file)

# run one file in one language
def run_file_in_lang(langdir, file):
	source = os.path.join(_source, langdir, file)
	content = read_content(source)
	filename = file
	title = None
	
	# markdown?
	if '.md' == os.path.splitext(file)[-1]:
		title = content.split('\n')[0]
		content = markdown.markdown(content, output_format='html5')
		filename = os.path.splitext(file)[0] + '.html'
	
	dump_content_to(content, title, langdir, filename)

# read content of a file into a string
def read_content(source):
	with io.open(source, 'r', encoding="utf-8") as handle:
		return handle.read()

# apply content and title to _template
def dump_content_to(content, title, langdir, target):
	lang = os.path.splitext(langdir)[0]
	_template.stream(title=title, content=content, lang=lang, target=target) \
		.dump(os.path.join(_target, langdir, target))

if '__main__' == __name__:
	run()
