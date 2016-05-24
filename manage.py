import os
from app import create_app, db  # , mysql
from app.models import TopStastic, WifiAp, PoiTypeOrder, BuildingRankByCity, BuildingRankByProvince
from flask.ext.script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, TopStastic=TopStastic, WifiAp=WifiAp, PoiTypeOrder=PoiTypeOrder,
                BuildingRankByCity=BuildingRankByCity, BuildingRankByProvince=BuildingRankByProvince)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Run the unit test."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


"""init the database:
@manager.command
def bssid_order_sync():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('select org_name,count(*) as count from bssid_org_name where org_name is not NULL group by org_name order by count desc')
    bssid_count = cursor.fetchall()
    index_count = 1
    for row in bssid_count:
        oui = WifiAp(id=index_count, oui=row[0], count=row[1])
        db.session.add(oui)
        db.session.commit()
        index_count = index_count + 1
    cursor.close()
    conn.close()

@manager.command
def poi_type_order_sync():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('select * from shop_type_order where shop_type is not NULL')
    poi_type_count = cursor.fetchall()
    index_count = 1
    for row in poi_type_count:
        poi = PoiTypeOrder(id=index_count, poi_type=row[0], count=row[1])
        db.session.add(poi)
        db.session.commit()
        index_count = index_count + 1
    cursor.close()
    conn.close()

@manager.command
def building_rank_by_city_sync():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('select * from rank_by_city')
    rank_city = cursor.fetchall()
    index_count = 1
    for row in rank_city:
        building_city = BuildingRankByCity(id=index_count, city=row[0], count=row[1], latitude=row[2], longitude=row[3])
        db.session.add(building_city)
        db.session.commit()
        index_count = index_count + 1
    cursor.close()
    conn.close()

@manager.command
def building_rank_by_province_sync():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('select * from rank_by_province')
    rank_province = cursor.fetchall()
    index_count = 1
    for row in rank_province:
        building_city = BuildingRankByProvince(id=index_count, province=row[0], count=row[1])
        db.session.add(building_city)
        db.session.commit()
        index_count = index_count + 1
    cursor.close()
    conn.close()
"""
if __name__ == '__main__':
    manager.run()
