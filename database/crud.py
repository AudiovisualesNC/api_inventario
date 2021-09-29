from sqlalchemy.orm import Session
import time
from datetime import datetime

from . import models, schemas


def get_room_by_hostname(db: Session, hostname: str):
    return db.query(models.Room).filter(models.Room.hostname == hostname).first()


def create_room(db: Session, room: schemas.RoomCreate):
    db_room = models.Room(room_id=room.room_id, ip=room.ip, hostname=room.hostname, room_name=room.room_name,
                          port_name=room.port_name, open_port=room.open_port, script_version=room.script_version,
                          with_button=room.with_button, operating_system=room.operating_system,
                          device=room.device, cam=room.cam, monitor=room.monitor, zone=room.zone,
                          province=room.province, office=room.office, building_name=room.building_name)
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room


def update_room(db: Session, new_room: schemas.RoomCreate, room: models.Room):
    room.room_id = new_room.room_id
    room.ip = new_room.ip
    room.hostname = new_room.hostname
    room.room_name = new_room.room_name
    room.port_name = new_room.port_name
    room.open_port = str(new_room.open_port)
    room.script_version = new_room.script_version
    room.with_button = str(new_room.with_button)
    room.operating_system = new_room.operating_system
    room.device = new_room.device
    room.cam = new_room.cam
    room.monitor = new_room.monitor
    room.zone = new_room.zone
    room.province = new_room.province
    room.office = str(new_room.office)
    room.building_name = new_room.building_name

    db.commit()
    db.refresh(room)
    return room


def update_last_connection(db: Session, room: models.Room):
    ts = time.time()
    timestamp = datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    room.last_connection = timestamp

    db.commit()
    return timestamp


def get_sala_by_roomid(db: Session, room_id: str):
    return db.query(models.Sala).filter(models.Sala.room_id == room_id).first()


def create_sala(db: Session, room: schemas.SalaCreate):
    db_room = models.Sala(room_id=room.room_id, room_name=room.room_name,
                          keypad=room.keypad, camara=room.camara, monitor=room.monitor)
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room