import os
import sys

from hudsonintegration.utils import system


def extract_name():
    """Return guessed package name.

    "/var/lib/hudson/jobs/lizard-map/workspace/trunk" -> lizard_map

    """
    cwd = os.getcwd()
    name = cwd.split('/jobs/')[1]
    name = name.split('/')[0]
    name = name.replace('-', '_')
    return name


def bin_dir():
    """Return the directory of the hudsonintegration buildout."""
    our_script = sys.argv[0]
    pathname = os.path.dirname(our_script)
    return os.path.abspath(pathname)


def go_to_checkout():
    """Go to the directory with the actual checkout."""
    contents = os.listdir('.')
    if len(contents) == 1:
        # We're in the workspace with one directory: the trunk checkout.
        # Chdir into it.
        os.chdir(contents[0])
    else:
        # Git checkout.
        pass


def run_tests():
    """Main method for the 'run_tests' command."""
    go_to_checkout()
    system("python bootstrap.py")
    system("bin/buildout -v")
    coverage = os.path.join(bin_dir(), 'coverage')
    system("%s run bin/test" % coverage)
    sys.exit(0)


def create_reports():
    """Main method for the 'create_reports' command."""
    package_name = extract_name() if len(sys.argv) < 2 else sys.argv[1]
    go_to_checkout()
    coverage = os.path.join(bin_dir(), 'coverage')
    pep8 = os.path.join(bin_dir(), 'pep8')
    pyflakes = os.path.join(bin_dir(), 'pyflakes')
    # Below: -r means recursive, it shows all instances of an error.
    # And we exclude generated django south migrations.
    pep8_args = '--exclude=migrations'
    if not 'NOREPEAT' in sys.argv:
        pep8_args += ' -r'
    system(("%s %s %s | " +
            "perl -ple 's/: [WE](\\d+)/: [W$1]/' > pep8.txt") % (
            pep8, pep8_args, package_name))
    system(("%s %s | " +
            "grep -v /migrations/ | " +
            "perl -ple 's/:\\ /: [E] /' >> pep8.txt") % (
            pyflakes, package_name))
    system("%s xml" % coverage)
    sys.exit(0)


def run_jslint():
    """Main method for the 'run_jslint' command."""
    go_to_checkout()
    jslint = os.path.join(bin_dir(), 'jslint')
    system("%s %s" % (jslint, extract_name()))
    sys.exit(0)
