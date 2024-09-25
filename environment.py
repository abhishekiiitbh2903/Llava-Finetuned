import sys

def check_environment():
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("Virtual Environment:", sys.prefix)
    else:
        print("System Environment:", sys.prefix)

check_environment()
