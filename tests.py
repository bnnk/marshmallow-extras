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
