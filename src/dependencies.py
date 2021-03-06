dependencies = ["pygame", "numpy", "cx-Freeze", "typing", "mypy", "colormath"]
dependencies.append("dill")

from sys import platform


if platform == "darwin":
    dependencies.append('pyobjc')
    dependencies.append('six')
    dependencies.append('appdirs')
    dependencies.append('AppKit')
