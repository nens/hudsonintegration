import os
import sys

from hudsonintegration.utils import system

RHINO = 'rhino'
JSLINT = os.path.abspath(os.path.join( os.path.dirname(__file__),
                                       'jslint.js'))


def main():
    if not len(sys.argv) > 1:
        print "Usage: jslint script1.js [script2.js...]"
        print "   or: jslint directory"
        sys.exit(1)

    javascript_files = sys.argv[1:]
    if len(javascript_files) == 1:
        possible_dir = javascript_files[0]
        if os.path.isdir(possible_dir):
            javascript_files = []
            for (dirpath, dirnames, filenames) in os.walk(possible_dir):
                javascript_files += [
                    os.path.join(dirpath, filename) for filename in filenames
                    if filename.endswith('.js')]

    for javascript_file in javascript_files:
        system('%s %s %s' % (RHINO, JSLINT, javascript_file))
    sys.exit(0)
