import datetime
from _typeshed import Incomplete

from pytz import UTC as UTC

class FixedOffset(datetime.tzinfo):
    def __init__(self, offset: float, name: str) -> None: ...
    def utcoffset(self, dt: datetime.datetime) -> datetime.timedelta: ...
    def tzname(self, dt: datetime.datetime) -> str: ...
    def dst(self, dt: datetime.datetime) -> datetime.timedelta: ...

STDOFFSET: datetime.timedelta
DSTOFFSET: datetime.timedelta

class LocalTimezone(datetime.tzinfo):
    def utcoffset(self, dt: datetime.datetime) -> datetime.timedelta: ...
    def dst(self, dt: datetime.datetime) -> datetime.timedelta: ...
    def tzname(self, dt: datetime.datetime) -> str: ...

Local: LocalTimezone
DSTSTART: datetime.datetime
DSTEND: datetime.datetime

def first_sunday_on_or_after(dt: datetime.datetime) -> datetime.datetime: ...

class USTimeZone(datetime.tzinfo):
    stdoffset: Incomplete
    reprname: Incomplete
    stdname: Incomplete
    dstname: Incomplete
    def __init__(self, hours: float, reprname: str, stdname: str, dstname: str) -> None: ...
    def tzname(self, dt: datetime.datetime) -> str: ...
    def utcoffset(self, dt: datetime.datetime) -> datetime.timedelta: ...
    def dst(self, dt: datetime.datetime) -> datetime.timedelta: ...

Eastern: USTimeZone
Central: USTimeZone
Mountain: USTimeZone
Pacific: USTimeZone
