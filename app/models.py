from app import db

"""class CityBuilding(db.Model):
    __tablename__ = 'building'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    province = db.Column(db.String, unique=True)
    city = db.Column(db.String)
    station = db.Column(db.Integer)
    airport = db.Column(db.Integer)
    metro = db.Column(db.Integer)
    hospital = db.Column(db.Integer)
    market = db.Column(db.Integer)
    office = db.Column(db.Integer)
    hotel = db.Column(db.Integer)
    museum = db.Column(db.Integer)
    exhabition = db.Column(db.Integer)
    library = db.Column(db.Integer)

    def __repr__(self):
        return '<City %r>' % self.city
"""


class TopStastic(db.Model):
    __tablename__ = 'topcount'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    building = db.Column(db.Integer)
    poi = db.Column(db.BigInteger)
    ap = db.Column(db.BigInteger)


"""class Poi(db.Model):
    __tablename__ = 'poi'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    province = db.Column(db.String, unique=True)
    city = db.Column(db.String)
    metro = db.Column(db.Integer)
    metro_gateway_in = db.Column(db.Integer)
    metro_gateway_out = db.Column(db.Integer)
    metro_service_point = db.Column(db.Integer)
    metro_intrance = db.Column(db.Integer)
    hospital_device_store = db.Column(db.Integer)
    hospital = db.Column(db.Integer)
    drugstore = db.Column(db.Integer)
    treatment_room = db.Column(db.Integer)
    doctor_office = db.Column(db.Integer)
    info_center = db.Column(db.Integer)
    locker_room = db.Column(db.Integer)
    rest_room = db.Column(db.Integer)
    finacial_office = db.Column(db.Integer)
    file_room = db.Column(db.Integer)
    duty_office = db.Column(db.Integer)
    apartment = db.Column(db.Integer)
    hotel = db.Column(db.BigInteger)
    accessories = db.Column(db.BigInteger)
    bank_service = db.Column(db.BigInteger)
    carwash = db.Column(db.BigInteger)
    cosmetic = db.Column(db.BigInteger)
    office = db.Column(db.BigInteger)
    private_building = db.Column(db.Integer)
    catering = db.Column(db.BigInteger)
    beatify = db.Column(db.BigInteger)
    entertainment = db.Column(db.BigInteger)
    shopping = db.Column(db.BigInteger)
    digital = db.Column(db.BigInteger)
    market = db.Column(db.BigInteger)
    travel = db.Column(db.Integer)
    home = db.Column(db.Integer)
    education = db.Column(db.BigInteger)
"""


class WifiAp(db.Model):
    __tablename__ = 'wifi'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # province = db.Column(db.String)
    # city = db.Column(db.String)
    oui = db.Column(db.String)
    count = db.Column(db.BigInteger)

    def __repr__(self):
        return '<Oui %r>' % self.oui


class PoiTypeOrder(db.Model):
    __tablename__ = 'poi_type_order'
    id = db.Column(db.Integer, primary_key=True)
    poi_type = db.Column(db.String)
    count = db.Column(db.Integer)


class BuildingRankByCity(db.Model):
    __tablename_ = 'building_rank_by_city'
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String)
    count = db.Column(db.Integer)
    latitude = db.Column(db.String)
    longitude = db.Column(db.String)


class BuildingRankByProvince(db.Model):
    __tablename__ = 'building_rank_by_province'
    id = db.Column(db.Integer, primary_key=True)
    province = db.Column(db.String)
    count = db.Column(db.Integer)
