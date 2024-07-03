from io import BytesIO
from struct import unpack
from ..General.GeneralClass import GeneralClass
from ..utils.getByte import getByte


class AddInt8YValue(GeneralClass):
    def __init__(self) -> None:
        super().__init__()
        self.operationName: str = "AddInt8YValue"
        self.operationNumber: int = 29
        self.value: int = 0

    def Marshal(self, writer: BytesIO) -> None:
        writer.write(self.value.to_bytes(length=1, byteorder="big", signed=True))

    def UnMarshal(self, buffer: BytesIO) -> None:
        self.value = unpack(">b", getByte(buffer, 1))[0]
