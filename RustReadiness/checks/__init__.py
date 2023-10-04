from os.path import dirname, basename, isfile, join
import glob
import importlib
import inspect

from RustReadiness.checks.IChecker import IChecker



checks = list(map(importlib.import_module, [ "RustReadiness.checks." + basename(f)[:-3] for f in glob.glob(join(dirname(__file__), "*.py")) if isfile(f) and not f.endswith('__init__.py')]))
check_list = []
for check in checks:
    classes = inspect.getmembers(check)
    try:
        for class_inst in classes:
            load_class = False
            for base in class_inst[1].__bases__:
                if base.__name__ == 'IChecker':
                    load_class = True
            if load_class:
                check_list.append(class_inst[1])
    except:
        pass