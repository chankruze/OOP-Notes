# import module (basic)
import my_module
my_module.func_in_module()

# import module as 'xyz' name
import my_module as me
me.func_in_module()

# import some specific functions from module
from my_module import func_in_module
func_in_module()

# NOT recommended
from my_module import *
func_in_module()
