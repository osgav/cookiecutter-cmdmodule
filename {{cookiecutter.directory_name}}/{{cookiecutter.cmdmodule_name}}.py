#!/usr/bin/env python
#
# osgav
#

import cmd
import os
import cmdsrc.echo as echo

INTRO_TEXT = """
---------------------------------------------
[+] {{cookiecutter.cmdmodule_name}}
---------------------------------------------

type ? or 'help' to view available commands and help topics

for more info on a command or help topic:
type ?command or 'help command'
type ?topic or 'help topic'
"""

USAGE_TEXT = """
usage: 

write detailed help on command
usage for {{cookiecutter.cmdmodule_name}} here 
"""


class {{cookiecutter.cmdmodule_name}}(cmd.Cmd):

    # shell
    #
    prompt = "cmd [] "
    def postcmd(self, stop, line):
        # print a new line after every command output
        # to save adding a print statement in every function...
        # print("")
        return cmd.Cmd.postcmd(self, stop, line)
    def emptyline(self):
        pass
    def help_shell(self):
        print("cmd [help] invoke a shell and run the provided command")
        print("cmd [help] e.g. 'shell ls' or 'shell date'")
        print("cmd [help] alternatively use the ! shortcut '!cal'")   
    def do_shell(self, line):
        print("cmd [shell] running command: %s\n" % line)
        output = os.popen(line).read()
        print output
        # self.last_output = output

    # help setup and 'help topic' commands
    #
    intro = INTRO_TEXT
    usage = USAGE_TEXT
    ruler = "-"
    doc_header = "commands:"
    misc_header = "\nhelp topics:"
    def help_intro(self):
        print(self.intro)
    def help_usage(self):
        print(self.usage)
    def help_help(self):
        print("cmd [help] list available commands with 'help' or detailed help with 'help cmd'")

    # exit commands
    #
    def help_exit(self):
        print("cmd [help] type 'exit', 'EOF' or hit Ctrl+D to shut this thing down")
    def do_exit(self, line):
        print("cmd [exit] goodbye!")
        return True
    do_EOF = do_exit
    help_EOF = help_exit


    # {{cookiecutter.cmdmodule_name}} commands
    #
    def do_echothis(self, line):
        self.mystring = line
        echo.ack()
    
    def do_echo(self, line):
        try:
            tada = getattr(self, "mystring")
            echo.say_stuff(tada)
        except AttributeError:
            print("you haven't run 'echothis' yet")

    def do_echobig(self, line):
        try:
            tada = getattr(self, "mystring")
            echo.shout_stuff(tada)
        except AttributeError:
            print("you haven't run 'echothis' yet")        




if __name__ == '__main__':
    {{cookiecutter.cmdmodule_name}}().cmdloop()
