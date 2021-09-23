from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .database import Base
from .schemas import Item, RoomCreate


class Room(Base):
    __tablename__ = "INVENTORY"

    id = Column(Integer, primary_key=True, index=True)
    ip = Column(String)
    hostname = Column(String, unique=True, index=True)
    room_id = Column(String)
    room_name = Column(String)
    port_name = Column(String, nullable=True)
    open_port = Column(String)
    script_version = Column(String)
    with_button = Column(String)
    operating_system = Column(String)
    device = Column(String)
    cam = Column(String)
    monitor = Column(String, nullable=True)
    zone = Column(String, nullable=True)
    province = Column(String, nullable=True)
    office = Column(String, nullable=True)
    building_name = Column(String, nullable=True)
    last_connection = Column(DateTime, nullable=True)
    record_created_at = Column(DateTime)

    def __eq__(self, other):
        """
        Se espera recibir un obejto RoomCreate para comparar, ya que se compara un objeto de la bbdd con uno recibido
        en el metodo POST de rooms
        :param other: Clase recibida para comparar
        :return:
        """
        if not isinstance(other, RoomCreate):
            return False
        else:
            return self.ip == other.ip and self.hostname == other.hostname and self.room_id == other.room_id \
               and self.room_name == other.room_name and self.port_name == other.port_name \
               and self.open_port == str(other.open_port) and self.script_version == other.script_version \
               and self.with_button == str(other.with_button) and self.operating_system == other.operating_system \
               and self.device == other.device and self.cam == other.cam and self.monitor == other.monitor \
               and self.zone == other.zone and self.province == other.province and self.office == other.office \
               and self.building_name == other.building_name
