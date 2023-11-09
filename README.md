# InBug - A debuger for your Python codes

A simple debuger for your python codes. You can use it to debug your codes and see the values of your variables in each line of your code.

```bash
# Installation
pip install inbug # Not yet available
```

# Usage

```python
from inbug import ib

# Configure the output prefix
ib().ConfigureOutput(prefix='InBug Debuger') # InBug Debuger: |

# Testing variables
a = 10
b = 20
ib(a) # InBug: | {'a': 10}
ib(b) # InBug: | {'b': 20}
ib(a, b) # InBug: | {'a': 10, 'b': 20}
ib(a, b, 30) # InBug: | {'a': 10, 'b': 20, None: 30}

# Testing kwargs
ib(a=10) # InBug: | {'a': 10}

ib().bug('Some bugs exists here.') # InBug: | /path/tp/folder/app.py:17 | Some bugs exists here.

```
