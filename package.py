name = "python.python_harvest_redux"
version = "2.1.0"

authors = []

description = \
"""
Pipeline Tools
"""

tools = []

requires = [
    "python"
]

variants = [
    ['default'],
]

config = {
    'build_directory': 'build/rez',
}

def commands():
    env.PYTHONPATH.append("{root}/python")
