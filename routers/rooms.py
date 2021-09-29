from fastapi import APIRouter, Body, Depends, HTTPException, status
from sqlalchemy.orm import Session

###En desarrollo
#from database import crud, models, schemas, database
### En produccion
from ..database import crud, models, schemas, database

router = APIRouter(

    prefix="/rooms",

    tags=["rooms"],

    # dependencies=[Depends(get_token_header)],

    responses={404: {"description": "Not found"}},

)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def new_room(room: schemas.Item, db: Session = Depends(get_db)):
    """
    :param room: Clase Item recibido a traves de la interfaz web de la sala
    :param db: Session para connectar a la base de datos
    :return:
    """
    """
        Como las claves del objeto JSON recibido de la interfaz web son distintos, primero lo recibo y convierto
        a una clase Item y luego lo paso a la clase RoomCreate, cuando se unifique los nombres de las variables este
        paso se puede saltar y recibir directamente un RoomCreate
    """
    room_create = schemas.RoomCreate(ip=room.ip, hostname=room.host, script_version=room.version,
                                     room_name=room.room_name, room_id=room.id, port_name=room.port,
                                     open_port=str(room.open_port),
                                     with_button=str(room.with_button), operating_system=room.windows,
                                     device=room.device,
                                     cam=room.cam, monitor=room.monitor, zone=room.zone, province=room.province,
                                     office=room.office, building_name=room.building_name)
    db_room = crud.get_room_by_hostname(db, hostname=room_create.hostname)
    db_sala = crud.get_sala_by_roomid(db, room_id=room_create.room_id)
    if not db_sala:
        salas_create = schemas.SalaCreate(room_name=room.room_name, room_id=room.id, keypad=room.with_button, camara=room.cam, monitor=room.monitor)
        crud.create_sala(db, salas_create)
    if db_room:
        if not db_room == room_create:
            return crud.update_room(db, room_create, db_room)
        else:
            return 201
    else:
        db_room = crud.create_room(db, room_create)
        if db_room:
            return db_room
        else:
            raise HTTPException(status_code=500, detail="Error saving in database")


@router.put("/lastconnection")
async def set_last_connection(hostname: str, db: Session = Depends(get_db)):
    db_room = crud.get_room_by_hostname(db, hostname=hostname)
    if db_room:
        return crud.update_last_connection(db, db_room)
    else:
        raise HTTPException(status_code=404, detail="Hostname not found")
