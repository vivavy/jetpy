#!/bin/env /usr/bin/python3
import os, sys, shutil, uuid


print(sys.argv)


try:shutil.rmtree("src/__pycache__")
except:pass
try:shutil.rmtree("../__pycache__")
except:pass

if sys.argv[0].startswith("py"):
    sys.argv = sys.argv[1:]

if "/" in sys.argv[0]:
    sys.argv[0] = sys.argv[0].split("/")[-1]

if sys.argv[0] != "jetpy" or len(sys.argv) not in (2, 3) or \
        sys.argv[1] not in ("build", "run", "debug"):
    print("using: jetpy ACTION")
    print("ACTION:")
    print("\tbuild\t-\tbuild project to *.jet file to ..")
    print("\trun\t-\trun project")
    print("\tdebug\t-\trun uncompiled project")
    sys.exit(0)

action = sys.argv[1]

if action == "debug":
    os.system(sys.executable + " /usr/jetpy/starter.py " + os.getcwd() + " src/main.py")

if action == "run":
    tmpdir = "/tmp/" + uuid.uuid4().hex[2:].replace("-", "")[::2]
    try:os.mkdir(tmpdir)
    except:pass
    shutil.unpack_archive(sys.argv[2], tmpdir, "zip")
    os.system(sys.executable + " /usr/jetpy/starter.py " + os.getcwd() + " " + tmpdir+"/src/main.py")
    try:shutil.rmtree(tmpdir)
    except:pass

if action == "build":
    tmpdir = "../" + uuid.uuid4().hex[2:].replace("-", "")[::2]
    shutil.copytree(os.path.abspath("."), tmpdir)
    os.system(sys.executable + " -m compileall " + tmpdir+"/src >/dev/null 2>&1")
    try:os.rename(tmpdir+"/src/__pycache__", tmpdir+"/src/__bytecode__")
    except:pass
    for f in os.listdir(tmpdir+"/src/__bytecode__"):
        try:os.rename(tmpdir+"/src/__bytecode__/"+f, tmpdir+"/src/"+f.split(".")[0]+"."+f.split(".")[-1])
        except:pass
    try:os.remove(tmpdir+"/jetpy")
    except:pass
    try:shutil.rmtree(tmpdir+"/src/__bytecode__")
    except:pass
    shutil.make_archive("../"+os.getcwd().split("/")[-1]+"", 'zip', tmpdir)
    os.rename("../"+os.getcwd().split("/")[-1]+".zip", "../"+os.getcwd().split("/")[-1]+".jet")
    shutil.rmtree(tmpdir)

try:shutil.rmtree("src/__pycache__")
except:pass
try:shutil.rmtree("../__pycache__")
except:pass
