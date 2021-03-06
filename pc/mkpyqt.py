#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2007-8 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 2 of the License, or
# version 3 of the License, or (at your option) any later version. It is
# provided for educational purposes and is distributed in the hope that
# it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See
# the GNU General Public License for more details.

######
## Original from Mark Summerfield, used in the book "Rapid GUI Programming with Python and Qt
## Edited by Lukas Hetzenecker
#####

import os
import stat
import sys
import PyQt4.QtCore

__version__ = "1.0.2"

app = PyQt4.QtCore.QCoreApplication([])
if sys.platform == "darwin":
   PATH = "/opt/local/bin"
   PYUIC4 = os.path.join(PATH, "pyuic4-2.5") # PYUIC4 = "/opt/local/bin/pyuic4-2.5" for installation from macports
   PYRCC4 = os.path.join(PATH, "pyrcc4-2.5")
   PYLUPDATE4 = os.path.join(PATH, "pylupdate4")
   LRELEASE = "lrelease-mac"
else:
   PATH = unicode(app.applicationDirPath())
   PYUIC4 = os.path.join(PATH, "pyuic4") # e.g. PYUIC4 = "/usr/bin/pyuic4"
   PYRCC4 = os.path.join(PATH, "pyrcc4")
   PYLUPDATE4 = os.path.join(PATH, "pylupdate4")
   LRELEASE = "lrelease-qt4"

del app
if sys.platform == "win32":
    PYUIC4 = PYUIC4.replace("/", "\\") + ".bat"
    PYRCC4 = PYRCC4.replace("/", "\\") + ".exe"
    PYLUPDATE4 = PYLUPDATE4.replace("/", "\\") + ".exe"

    PYUIC4LIB = os.path.join(PATH, "Lib/site-packages/PyQt4/bin/pyuic4")
    PYRCC4LIB = os.path.join(PATH, "Lib/site-packages/PyQt4/bin/pyrcc4")
    PYLUPDATE4LIB = os.path.join(PATH, "Lib/site-packages/PyQt4/bin/pylupdate4")
    PYUIC4LIB = PYUIC4LIB.replace("/", "\\") + ".bat"
    PYRCC4LIB = PYRCC4LIB.replace("/", "\\") + ".exe"
    PYLUPDATE4LIB = PYLUPDATE4LIB.replace("/", "\\") + ".exe"

msg = []
if not os.access(PYUIC4, os.F_OK):
    msg.append("failed to find pyuic4; tried %s " % PYUIC4)
if not os.access(PYRCC4, os.F_OK):
    msg.append("failed to find pyrcc4; tried %s" % PYRCC4)
if not os.access(PYLUPDATE4, os.F_OK):
    msg.append("failed to find pylupdate4; tried %s" % PYLUPDATE4)

msglib = []
if sys.platform == "win32":
    if os.access(PYUIC4LIB, os.F_OK):
        PYUIC4 = PYUIC4LIB
    else:
        msglib.append("failed to find pyuic4; tried %s " % PYUIC4LIB)

    if os.access(PYRCC4LIB, os.F_OK):
        PYRCC4 = PYRCC4LIB
    else:
        msglib.append("failed to find pyrcc4; tried %s" % PYRCC4LIB)
    if os.access(PYLUPDATE4LIB, os.F_OK):
        PYLUPDATE4 = PYLUPDATE4LIB
    else:
        msglib.append("failed to find pylupdate4; tried %s" % PYLUPDATE4LIB)

if msg and msglib:
    print "\n".join(msg).join("\n").join(msglib)
    print "try manually editing this program to put the correct " + \
          "paths in place"
    sys.exit()

Debug = False
Verbose = False

def usage():
    print """usage: mkpyqt.py [options] [path]

Options (which can be given in any of the forms shown):
-b  --build      build [default]
-c  --clean      clean
-f  --force      force
-t  --translate  translate
-r  --recurse    recurse
-v  --verbose    verbose
-D  --debug      debug

If executed with no arguments (or with a build argument) it does a
build, i.e., it looks for all *.ui and *.qrc files and makes sure that
the corresponding ui_*.py and qrc_*.py files exist and are up-to-date.

If executed with clean, deletes all ui_*.py and qrc_*.py files that have
corresponding *.ui and *.qrc files, and all *.pyc and *.pyo files.

If executed with force, it does a clean followed by a build.

If building and the translate option is given, after building, it runs
pylupdate4 on all .py and .pyw files it encounters, and then runs lrelease
on all .ts files it encounters. It does not use a .pro file so the .ts
files must be created in the first place, e.g., using pylupdate4 on one
of the source files and using its -ts option.

WARNING: Do not give any hand-coded files names that match ui_*.py or
qrc_*.py since these will be deleted by mkpyqt.py clean!

NOTE: If any tool fails to run, e.g., pyuic4, then edit this program and
hard-code the path; the variables with the tool paths are near the top
of the file.

mkpyqt.py v %s. Copyright (c) 2007 Qtrac Ltd. All rights reserved.
""" % __version__
    sys.exit()


def build(path):
    # make translation first
    command = LRELEASE
    args = ["series60-remote.pro"]

    process = PyQt4.QtCore.QProcess()
    process.start(command, args)
    if not process.waitForFinished(2 * 60 * 1000):
        print "failed", command, " ".join(args)

    # Also update Qt translations
    for file in os.listdir(path + "lang/"):
       if file.startswith("qt_") and file.endswith(".ts"):
          command = LRELEASE
          args = [path + "lang/" + file, "-qm", path + "lang/" + file[:-3] + ".qm"]
          process = PyQt4.QtCore.QProcess()
          process.start(command, args)
          if not process.waitForFinished(2 * 60 * 1000):
             print "failed", command, " ".join(args)

    # then build ui/qrc files
    search_path = path + "ui/src"
    dest = path + "ui"

    for name in os.listdir(search_path):
        source = os.path.join(search_path, name)
        target = "./"
        if source.endswith(".ui"):
            target += os.path.join(dest, "ui_" + name.replace(".ui", ".py"))
            command = PYUIC4
        elif source.endswith(".qrc"):
            target += os.path.join(dest, name.replace(".qrc", "") + "_rc.py")
            command = PYRCC4
        process = PyQt4.QtCore.QProcess()
        if target is not "./":
            if not os.access(target, os.F_OK) or (os.stat(source)[stat.ST_MTIME] > os.stat(target)[stat.ST_MTIME]) or \
                source.endswith(".qrc"): # Always update resource files

                args = ["-o", target, source]
                if Debug:
                    print "# %s -o %s %s" % (command, target, source)
                else:
                    process.start(command, args)
                    if not process.waitForFinished(2 * 60 * 1000):
                        print "failed", command, " ".join(args)
                    else:
                        print source, "->", target
            elif Verbose:
                    print source, "is up-to-date"

def clean(path):
    myPath = "./"
    deletelist = []
    for dir in os.listdir(myPath):
        if not os.path.isdir(myPath + dir):
            continue
        path = myPath + dir
        for name in os.listdir(myPath + dir):
            path = myPath + dir
            target = os.path.join(path, name)
            source = None
            if target.endswith(".py") or target.endswith(".pyc") or \
               target.endswith(".pyo"):
                if name.startswith("ui_")  and not name[-1] in "oc":
                    source = os.path.join(path + "/src", name[3:-3] + ".ui")
                elif name.endswith("_rc.py"):
                    if target[-1] in "oc":
                        source = os.path.join(path + "/src", name[0:-7] + ".qrc")
                    else:
                        source = os.path.join(path + "/src", name[0:-6] + ".qrc")
                elif target[-1] in "oc":
                    source = target[:-1]
                if source is not None:
                    if os.access(source, os.F_OK):
                        if Debug:
                            print "# delete ", target
                        else:
                            deletelist.append(target)
                    else:
                        print "will not remove '%s' since `%s' not found" % (
                                target, source)
        if not Debug:
            for target in deletelist:
                if Verbose:
                    print "deleted", target
                try:
                    os.remove(target)
                except:
                    pass

def translate(path):
    command1 = PYLUPDATE4
    args1 = ["-verbose", "series60-remote.pro"]
    command2 = LRELEASE
    args2 = ["series60-remote.pro"]

    process = PyQt4.QtCore.QProcess()
    process.start(command1, args1)
    if not process.waitForFinished(2 * 60 * 1000):
        print "failed", command1, " ".join(args1)
    process.start(command2, args2)
    if not process.waitForFinished(2 * 60 * 1000):
        print "failed", command2, " ".join(args2)

    # Also update Qt translations
    for file in os.listdir(path + "lang/"):
       if file.startswith("qt_") and file.endswith(".ts"):
          command = LRELEASE
          args = [path + "lang/" + file, "-qm", path + "lang/" + file[:-3] + ".qm"]
          process = PyQt4.QtCore.QProcess()
          process.start(command, args)
          if not process.waitForFinished(2 * 60 * 1000):
             print "failed", command, " ".join(args)

def apply(recurse, function, path):
    if not recurse:
        function(path)
    else:
        for root, dirs, files in os.walk(path):
            for dir in dirs:
                function(os.path.join(root, dir))


def main():
    global Debug, Verbose
    function = build
    recurse = False
    trans = False
    force = False
    path = ""
    args = sys.argv[1:]
    while args:
        arg = args.pop(0)
        if arg in ("-D", "--debug", "debug"):
            Debug = True
        elif arg in ("-b", "--build", "build"):
            pass # This is the default
        elif arg in ("-c", "--clean", "clean"):
            function = clean
        elif arg in ("-f", "--force", "force"):
            force = True
        elif arg in ("-t", "--translate", "translate"):
            trans = True
        elif arg in ("-r", "--recurse", "recurse"):
            recurse = True
        elif arg in ("-v", "--verbose", "verbose"):
            Verbose = True
        elif arg in ("-h", "--help", "help"):
            usage()
        else:
            path = arg
    if trans and (function == build or force):
        apply(recurse, translate, path)
    if not force:
        apply(recurse, function, path)
    else:
        apply(recurse, clean, path)
        apply(recurse, build, path)

main()

# 1.0.1 Fixed bug reported by Brian Downing where paths that contained
#       spaces were not handled correctly.
