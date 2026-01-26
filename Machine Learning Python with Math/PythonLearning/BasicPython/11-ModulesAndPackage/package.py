# ## Python packages must have __init__.py file to be recognized as packages

# __init__.py file can be empty or can execute initialization code for the package.
# # package.py
# # This is the __init__.py file for the package
# print("Package initialized")
# # You can export certain modules or functions here
# from .module1 import function1
# from .module2 import function2
# # Now when you import the package, these functions will be available directly
# # Example usage:
# # from package import function1, function2