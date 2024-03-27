#!/bin/env /usr/bin/python3
import os, sys, shutil, uuid


start = True

try:shutil.rmtree("src/__pycache__")
except:pass
try:shutil.rmtree("../__pycache__")
except:pass

if sys.argv[0].startswith("py"):
    sys.argv = sys.argv[1:]

if "/" in sys.argv[0]:
    sys.argv[0] = sys.argv[0].split("/")[-1]

if sys.argv[-1] == "--loadonly":
    sys.argv.pop()
    start = False
else:
    start = True

if sys.argv[-1] == "--mswin":
    sys.argv.pop()
    base = "C:\\Jetpy\\"
    temp = f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Temp\\"
else:
    base = "/usr/jetpy/"
    temp = "/tmp/"

if sys.argv[-1] == "--loadonly" and not start:
    sys.argv.pop()
    start = False
else:
    start = True

if sys.argv[0] != "jetpy" or len(sys.argv) not in (2, 3) or \
        sys.argv[1] not in ("build", "run", "debug"):
    print("using: jetpy ACTION")
    print("ACTION:")
    print("\tbuild\t-\tbuild project to *.jet file to ..")
    print("\trun\t-\trun project")
    print("\tdebug\t-\trun uncompiled project")
    sys.exit(0)

action = sys.argv[1]

if action == "load":
    tmpdir = temp + uuid.uuid4().hex[2:].replace("-", "")[::2]
    try:os.mkdir(tmpdir)
    except FileExistsError: pass
    shutil.unpack_archive(sys.argv[2], tmpdir, "zip")
    open("/tmp/jetpy_path", "wt").write(tmpdir)
    sys.exit()

if action == "debug":
    os.system(sys.executable + f" {base}starter.py" +
              (" --mswin" if "\\" in base else "") + 
              (" --initonly" if not start else "") + " " + os.getcwd() + " src/main.py")
    sys.exit()

if action == "run":
    tmpdir = temp + uuid.uuid4().hex[2:].replace("-", "")[::2]
    try:os.mkdir(tmpdir)
    except:pass
    shutil.unpack_archive(sys.argv[2], tmpdir, "zip")
    os.system(sys.executable + f" {base}starter.py " + tmpdir + (" --mswin" if "\\" in base else "")
              + " " + os.getcwd() +  
              (" --initonly" if not start else "") + " " + tmpdir+"src/main.py")
    try:shutil.rmtree(tmpdir)
    except:pass
    sys.exit()

if action == "build":
    tmpdir = "../" + uuid.uuid4().hex[2:].replace("-", "")[::2]
    shutil.copytree(os.path.abspath("."), tmpdir)
    os.system(sys.executable + " -m compileall " + tmpdir+"src >/dev/null 2>&1")
    try:os.rename(tmpdir+"/src/__pycache__", tmpdir+"/src/__bytecode__")
    except:pass
    for f in os.listdir(tmpdir+"src/__bytecode__"):
        try:os.rename(tmpdir+"src/__bytecode__/"+f,
                      tmpdir+"src/"+f.split(".")[0]+"."+f.split(".")[-1])
        except:pass
    try:os.remove(tmpdir+"jetpy")
    except:pass
    try:shutil.rmtree(tmpdir+"src/__bytecode__")
    except:pass
    shutil.make_archive("../"+os.getcwd().split("/")[-1]+"", 'zip', tmpdir)
    os.rename("../"+os.getcwd().split("/")[-1]+".zip", "../"+os.getcwd().split("/")[-1]+".jet")
    shutil.rmtree(tmpdir)
    sys.exit()

try:shutil.rmtree("src/__pycache__")
except:pass
try:shutil.rmtree("../__pycache__")
except:pass
