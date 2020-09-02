import enum

from flask_sqlalchemy import SQLAlchemy

from .views import app

# Create database connection object
db = SQLAlchemy(app)

class Color(enum.Enum):
    unknown = 0
    brown   = 1
    blue    = 2
    black   = 3
    silver  = 4
    red     = 5
    white   = 6
    green   = 7
    beige   = 8
    yellow  = 9
    orange  = 10
    gold    = 11
    violet  = 12

class Transmission(enum.Enum):
    unknown = 0
    man     = 1
    auto    = 2

class Fuel(enum.Enum):
    unknown  = 0
    diesel   = 1
    gasoline = 2
    lpg      = 3
    cng      = 4

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    maker = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    mileage = db.Column(db.Integer(), nullable=False)
    manufacture_year = db.Column(db.Integer(), nullable=False)
    engine_displacement = db.Column(db.Integer(), nullable=False)
    engine_power = db.Column(db.Integer(), nullable=False)
    color_slug = db.Column(db.Enum(Color), nullable=False)
    transmission = db.Column(db.Enum(Transmission), nullable=False)
    door_count = db.Column(db.Integer(), nullable=False)
    seat_count = db.Column(db.Integer(), nullable=False)
    fuel_type = db.Column(db.Enum(Fuel), nullable=False)
    price_eur = db.Column(db.Float(precision=2), nullable=False)

    def __init__(self, maker,
                       model,
                       mileage,
                       manufacture_year,
                       engine_displacement,
                       engine_power,
                       color_slug,
                       transmission,
                       door_count,
                       seat_count,
                       fuel_type,
                       price_eur):
        self.maker = maker
        self.model = model
        self.mileage = mileage
        self.manufacture_year = manufacture_year
        self.engine_displacement = engine_displacement
        self.engine_power = engine_power
        self.color_slug = color_slug
        self.transmission = transmission
        self.door_count = door_count
        self.seat_count = seat_count
        self.fuel_type = fuel_type
        self.price_eur = price_eur

    def __init__(self, pandas_serie):
        self.maker = pandas_serie['maker']
        self.model = pandas_serie['model']
        self.mileage = pandas_serie['mileage']
        self.manufacture_year = pandas_serie['manufacture_year']
        self.engine_displacement = pandas_serie['engine_displacement']
        self.engine_power = pandas_serie['engine_power']
        self.color_slug = Color[pandas_serie['color_slug']]
        self.transmission = Transmission[pandas_serie['transmission']]
        self.door_count = pandas_serie['door_count']
        self.seat_count = pandas_serie['seat_count']
        self.fuel_type = Fuel[pandas_serie['fuel_type']]
        self.price_eur = pandas_serie['price_eur']

def cast_dataframe_types(df):
    df = df.astype({
        'mileage': 'int32',
        'manufacture_year': 'int32',
        'engine_displacement': 'int32',
        'engine_power': 'int32',
        'door_count': 'int32',
        'seat_count': 'int32',
    })
    for name, enum_class in zip(['color_slug', 'transmission', 'fuel_type'],
                                [Color, Transmission, Fuel]):
        df.loc[~df[name].isin([e.name for e in enum_class]), name] = 'unknown'

    return df