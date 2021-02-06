from os import path, listdir, curdir
from re import match
from startuper import StartUper


if __name__ == "__main__":
    files = [f for f in filter(path.isfile, listdir(curdir)) if match(r'.*\.(csv|json|xml)', f)]
    strartuper = StartUper(files)
    strartuper.run()
