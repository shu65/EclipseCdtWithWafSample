#! /usr/bin/env python
# encoding: utf-8

VERSION='0.0.1'
APPNAME='EclipseCdtWithWaf'

top = '.'
out = 'build'

from waflib.extras import eclipse

def options(opt):
	opt.load('compiler_cxx')

def configure(conf):
	conf.load('compiler_cxx')
	conf.env.CXXFLAGS += ['-O2', '-Wall', '-W', '-g']
#	conf.check(header_name='stdio.h', features='cxx cxxprogram', mandatory=False)

def build(bld):
	bld.program(features='cxx cxxprogram', source='src/helloworld.cpp', target='helloworld')
	#bld.recurse("src")

