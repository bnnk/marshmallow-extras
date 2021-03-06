# marshmallow-extras
## Extras for marshmallow.

![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg) ![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)

[![codecov](https://codecov.io/gh/bnnk/marshmallow-extras/branch/master/graph/badge.svg)](https://codecov.io/gh/bnnk/marshmallow-extras) [![Build Status](https://travis-ci.com/bnnk/marshmallow-extras.svg?branch=master)](https://travis-ci.com/bnnk/marshmallow-extras)

marshmallow-extras is a python package which helps in serialization of heavy and hardcore objects easily using marshmallow (cause this is a plugin for marshmallow)

Travis Status:
<embed src="https://travis-ci.com/github/bnnk/marshmallow-extras" />


## Installing

### Using Github
```bash
git clone https://github.com/bnnk/marshmallow-extras
cd marshmallow-extras
pip install -e .
```

or use the `install/linux.sh.sh` (on linux) or `install/windows.bat` (on windows)

### Using PyPI

```bash
pip install marshmallow-extras
```
## Testing the installation
1. Copy the code from here and paste it into a file.
```python
from mshextras import *
import pyotp
import pandas as pd
import numpy as np
from requests import get
from xml.etree import ElementTree as ET
from furl import furl
from marshmallow import Schema
class TestingSchema(Schema):
    furl = FurlField()
    df = PandasDataFrameField()
    arr = NumPyArrayField()
    req = HTTPRequestField()
    et = ElementTreeField()
    ho = HOTPField()
    to = TOTPField()
ent = dict(
    furl = furl("bz2://"),
    df = pd.DataFrame({"a" : ["12"], "B" : ["13"]}),
    arr = np.array([1,2,3,4,5]),
    req = get("http://google.com"),
    ho = pyotp.hotp.HOTP(pyotp.random_base32()),
    to = pyotp.totp.TOTP(pyotp.random_base32())
)
print(TestingSchema().dump(ent))
print(TestingSchema().load(TestingSchema().dump(ent)))
```
2. Install the package (this should install all the required child packages.
3. Run the file.

## Package Details
This package has the following classes
> FurlField - Field for Furl Objects [(read more about this package here)](https://github.com/gruns/furl/blob/master/README.md)

> PandasDataFrameField - Field for pandas Dataframe

> NumPyArrayField - Field for numpy arrays

> HTTPRequestField - Field for Requests's get(),post(),put() or request() method's Response class

> ElementTreeField - Field for xml.etree.ElementTree objects

> HOTPField - Field for PyOTP's HOTP objects

> TOTPField - Field for PyOTP's TOTP objects
