#! /usr/bin/env python

import inspect, os

from subprocess import call

def run_cmd(cmd):
    print "Executing system command:"
    print " ".join(cmd)
    call(cmd)


def create_directory(directory):
    if os.path.exists(directory):
        print "Exists: " + directory
    else:
        print "Creating " + directory
        os.mkdir(directory)

def create_in_home_directory(directory):
    create_directory(os.environ["HOME"] + "/" + directory)

def switch_ruby_script_path():
    return os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + "/switch-ruby"



exec_paths = os.environ["PATH"].split(":")
i = 0
for path in exec_paths:
    highlight = ""
    if os.access(path, os.W_OK):
        highlight = "\x1b[32m" #foo\x1b[0m"

    print highlight + str(i) + ": " + path + "\x1b[0m"
    i = i + 1

path_index = raw_input('Where should a sym-link to the switch-ruby script be created (green has write permissions): ')


run_cmd(["ln", "-nfs", switch_ruby_script_path(), exec_paths[int(path_index)] + "/"])


print "Preparing directories..."
create_in_home_directory(".rb")
create_in_home_directory(".rb/cache")
create_in_home_directory(".rb/src")


print "Finished."

print "Add the following line at the end of your ~/.bashrc file:"
print "export PATH=$HOME/.rb/bin:$PATH"

