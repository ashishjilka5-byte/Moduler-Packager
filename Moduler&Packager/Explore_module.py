import importlib

def explore_module_attributes():
    print("Explore Module Attributes:")
    module_name = input("Enter module name to explore: ")
    module = importlib.import_module(module_name)
    print("Available Attributes in", module_name, "module:")
    print(dir(module))

