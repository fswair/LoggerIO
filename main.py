from io import StringIO
from typing import TextIO
from enum import Enum
import sys


class LogLevels(Enum):
    INFO = auto()
    WARN = auto()
    ERROR = auto()
    DEFAULT = auto()


class LoggerIO(object):
    def __init__(self, name: str = __name__, buffer: TextIO = sys.stdout):
        self.buffer = buffer

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def log(
        self, message: str, level: LogLevels = LogLevels.DEFAULT, io_mode: str = "a"
    ) -> "LoggerIO":
        prefix = ""
        match (level):
            case LogLevels.INFO:
                prefix = "[INFO]"
            case LogLevels.WARN:
                prefix = "[WARN]"
            case LogLevels.ERROR:
                prefix = "[ERROR]"
            case (_, LogLevels.DEFAULT):
                prefix = "[LOG]"
        self.buffer.mode = io_mode
        io = StringIO(f"{prefix} {message}\n")
        
        self.buffer.write(io.read())
        return LoggerIO(buffer=self.buffer)

    def __repr__(self):
        return """logger.log('Instance created!', level=LogLevels.INFO)"""
