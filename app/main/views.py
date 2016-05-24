from flask import render_template, jsonify, session, redirect, url_for, current_app
from . import main
from .. import db
from ..models import TopStastic, WifiAp, PoiTypeOrder, BuildingRankByCity, BuildingRankByProvince
import re


@main.route('/')
def index():
    top_count = TopStastic.query.first()
    building_cnt = top_count.building
    poi_cnt = top_count.poi
    ap_cnt = top_count.ap

    return render_template('index.html', building=building_cnt, poi=poi_cnt, ap=ap_cnt)


@main.route('/wifi/')
def wifi():
    return render_template('wifi.html')


@main.route('/poi/')
def poi():
    return render_template('poi.html')


@main.route('/development/')
def development():
    return render_template('development.html')


@main.route('/building/map/test')
def building_map_test():
    return render_template('building.html')


@main.route('/about/intro')
def intro():
    return render_template('intro.html')


@main.route('/about/contact')
def contact():
    return render_template('contact.html')


"""simple REST: """


@main.route('/api/v1.0/building/rank/city', methods=['GET'])
def get_rank_by_city():
    query_result = BuildingRankByCity.query.all()
    city_rank = []
    for row in query_result:
        crg = {'city': row.city, 'count': row.count, 'lat': row.latitude, 'long': row.longitude}
        city_rank.append(crg)

    return jsonify(result=city_rank)


@main.route('/api/v1.0/wifi/oui/order', methods=['GET'])
def get_wifi_order():
    query_result = WifiAp.query.all()
    wifi_order = []
    for row in query_result:
        if row.count > 5000:
            wo = {'oui': row.oui, 'count': row.count}
            wifi_order.append(wo)

    return jsonify(result=wifi_order)


@main.route('/api/v1.0/poi/type', methods=['GET'])
def get_poi_type_order():
    query_result = PoiTypeOrder.query.all()
    type_order = []
    for row in query_result:
        pto = {'type': row.poi_type, 'count': row.count}
        type_order.append(pto)

    return jsonify(result=type_order)
