#!/usr/bin/env python3
#
#  Uses HTML data from _source and renders them, using Jinja2, into _target
#
#  Requirements:
#  - jinja2
#  - markdown

_template_dir = 'templates'
_template_name = 'base.html'
_source = 'c-tracker-sccs-content'
_target = '.'
_files = [
	'index.html',
	'team.md',
	'AboutSCCS.md',
	'PrivacyPolicy.md',
	'LicenseAgreement.md',
]

if '__main__' == __name__:
	exec(open('c-tracker-sccs-content/build.py').read())
	run(_template_dir, _template_name, _source, _target, _files)
