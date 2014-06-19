import os
from src.package import Package

def list_subdir(dir):
    return [name for name in os.listdir(dir)
            if os.path.isdir(os.path.join(dir, name))]