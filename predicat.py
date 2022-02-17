import click
from cli import *

@click.command()
@click.option('-c', '--command', is_flag=True, help='display explicitely the history of the code execution.')
@click.argument("name")
def outil(name: str, debug: bool, verbose: bool, grammar: bool):
    if command == True:
       run("check A B C")
    else:
        MyPrompt().cmdloop()
        

if __name__ == '__main__':
    outil(prog_name='outil')
