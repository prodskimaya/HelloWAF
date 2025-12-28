APPNAME = "HelloWAF"
VERSION = "1.0"

top = "."
out = "build"

def options(opt):
        opt.load('compiler_cxx')

def configure(ctx):
	ctx.load('compiler_cxx')
	print("Configuring project in", ctx.path.abspath())

def dist(ctx):
	ctx.algo = "zip"

def build(bld):
	bld.program(source="src/main.cpp", includes="include", target=APPNAME)
