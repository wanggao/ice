#!/usr/bin/env python
# **********************************************************************
#
# Copyright (c) 2003-2006 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

import os, sys

for toplevel in [".", "..", "../..", "../../..", "../../../.."]:
    toplevel = os.path.normpath(toplevel)
    if os.path.exists(os.path.join(toplevel, "config", "TestUtil.py")):
        break
else:
    raise "can't find toplevel directory!"

sys.path.append(os.path.join(toplevel, "config"))
import TestUtil
import IceGridAdmin

name = os.path.join("IceGrid", "deployer")
testdir = os.path.join(toplevel, "test", name)

if TestUtil.isWin32():
    os.environ["PATH"] = testdir + ";" + os.getenv("PATH", "")
elif TestUtil.isAIX():
    os.environ["LIBPATH"] = testdir + ":" + os.getenv("LIBPATH", "")
else:
    os.environ["LD_LIBRARY_PATH"] = testdir + ":" + os.getenv("LD_LIBRARY_PATH", "")
    os.environ["LD_LIBRARY_PATH_64"] = testdir + ":" + os.getenv("LD_LIBRARY_PATH_64", "")

iceBox = TestUtil.getIceBox(testdir)

IceGridAdmin.iceGridTest(name, "application.xml", "", '"icebox.exe=' + TestUtil.getIceBox(testdir) + '"')

# Tests with targets
IceGridAdmin.iceGridTest(name, "application.xml", "-t", \
                         "icebox.exe=" + TestUtil.getIceBox(testdir) + \
                         " moreservers moreservices moreproperties")

sys.exit(0)
