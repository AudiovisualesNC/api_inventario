from typing import List, Optional

from pydantic import BaseModel
from pydantic.schema import datetime


class RoomBase(BaseModel):
    ip: str
    hostname: str
    script_version: str
    room_name: str
    room_id: str
    port_name: Optional[str] = None
    open_port: str
    with_button: str
    operating_system: str
    device: str
    cam: str
    monitor: Optional[str] = None
    zone: Optional[str] = None
    province: Optional[str] = None
    office: Optional[str] = None
    building_name: Optional[str] = None


class RoomCreate(RoomBase):
    pass


class Room(RoomBase):
    id: int
    last_connection: Optional[datetime] = None
    record_created_at: datetime

    class Config:
        orm_mode = True


class Item(BaseModel):
    ip: str
    host: str
    version: str
    room_name: str
    id: str
    port: Optional[str] = None
    open_port: bool
    with_button: bool
    windows: str
    device: str
    cam: str
    monitor: Optional[str] = None
    zone: Optional[str] = None
    province: Optional[str] = None
    office: Optional[str] = None
    building_name: Optional[str] = None


class SalaBase(BaseModel):
    room_name: str
    room_id: str
    keypad: bool
    camara: str
    monitor: Optional[str] = None
    id_edificio: Optional[int] = None


class SalaCreate(SalaBase):
    pass


class Sala(SalaBase):
    id: int
    calendar: Optional[str] = None
    nota: Optional[str] = None

    class Config:
        orm_mode = True
