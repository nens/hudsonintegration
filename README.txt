hudsonintegration: scripts for Jenkins
======================================

Small collection of scripts that shorten the build steps that we have
to configure Jenkins with.

Every project in Jenkins needs a couple of build steps. When we just
started out, you'd copy another projects's settings and change
everything from "lizard-abc" to "lizard-xyz" seven times or so.
That's why we have a couple of scripts here that auto-detect things
and work from N&S-internal conventions.  ("Convention" mostly means
"that's what hudsonintegration expects so that's what we do", but ok).

Available commands
------------------

- **run_tests**: run bootstrap, buildout and run the tests in coverage
  mode.

- **create_reports**: create xml coverage report and a pep8/pyflakes report
  for Jenkins' reporting statistics. Pass 'NOREPEAT' (without the quotes) as a
  command line option to ``create_reports`` if you don't want pep8 to report
  on every error, but just on the first error.

- **run_jslint**: run jslint on the package.  Works fine if there are
  only custom javascripts inside the package directory.  If there are
  external libraries, too, you have to call jslint yourself on just
  the custom files.  See lizard-ui's Jenkins settings.

- **jslint**: run the included ``jslint.js`` with "rhino".  Wrapper as
  jslint itself is not handily installable otherwise.


Installation
------------

Hudsonintegration is installed on buildbot.lizardsystem.nl in
``/var/lib/jenkins/hudsonintegration``.
