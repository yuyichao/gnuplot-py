# $Id$

# Copyright (C) 1998-2003 Michael Haggerty <mhagger@alum.mit.edu>
#
# This file is licensed under the GNU Lesser General Public License
# (LGPL).  See LICENSE.txt for details.

"""gp -- a platform-independent interface to a gnuplot process.

This file imports a low-level, platform-independent interface to the
gnuplot program.  Which interface is imported depends on the platform.
There are variations of this file for Unix, the Macintosh, and for
Windows called gp_unix.py, gp_mac.py, and gp_win32.py, respectively.
Note that the end-user should use the more capable interface from
__init__.py (i.e., 'import Gnuplot') rather than the low-level
interface imported by this file.

See gp_unix.py for most documentation about the facilities of the
gp_*.py modules.

"""

import sys

# Low-level communication with gnuplot is platform-dependent.  Import
# the appropriate implementation of GnuplotProcess based on the
# platform:
if sys.platform == 'mac':
    try:
        from .gp_mac import GnuplotOpts, GnuplotProcess, test_persist
    except ValueError:
        from gp_mac import GnuplotOpts, GnuplotProcess, test_persist
elif sys.platform == 'win32':
    try:
        from .gp_win32 import GnuplotOpts, GnuplotProcess, test_persist
    except ValueError:
        from gp_win32 import GnuplotOpts, GnuplotProcess, test_persist
elif sys.platform == 'darwin':
    try:
        from .gp_macosx import GnuplotOpts, GnuplotProcess, test_persist
    except ValueError:
        from gp_macosx import GnuplotOpts, GnuplotProcess, test_persist
elif sys.platform[:4] == 'java':
    try:
        from .gp_java import GnuplotOpts, GnuplotProcess, test_persist
    except ValueError:
        from gp_java import GnuplotOpts, GnuplotProcess, test_persist
elif sys.platform == 'cygwin':
    try:
        from .gp_cygwin import GnuplotOpts, GnuplotProcess, test_persist
    except ValueError:
        from gp_cygwin import GnuplotOpts, GnuplotProcess, test_persist
else:
    try:
        from .gp_unix import GnuplotOpts, GnuplotProcess, test_persist
    except ValueError:
        from gp_unix import GnuplotOpts, GnuplotProcess, test_persist


def double_quote_string(s):
    """Return string s quoted and surrounded by double-quotes for gnuplot."""

    for c in ['\\', '\"']:
        s = s.replace(c, '\\' + c)

    return '"%s"' % (s,)
