from flask import Flask
from flask import jsonify


HANGOVER_RATING = 0
BODYWEIGHT = 1.0
DRINK_UNITS = 0.0
WARNING_THREASHOLD = 3.0
ULTRA_HANGOVER_WARNING_THREASHOLD = 6.0
ULTRA_HANGOVER_RATING = 7


app = Flask(__name__)


@app.route('/')
def check_hangover():
    return "current drink units: {}".format(DRINK_UNITS)


@app.route('/RegisterHangover/<hangover_rating>')
def register_hangover(hangover_rating):
    global HANGOVER_RATING
    HANGOVER_RATING = hangover_rating
    return jsonify({"ok": True})


@app.route('/RegisterBodyweight/<bodyweight_unit>/<bodyweight>')
def register_bodyweight(bodyweight_unit, bodyweight):
    global BODYWEIGHT
    BODYWEIGHT = normalize_bodyweight(bodyweight_unit, bodyweight)
    return jsonify({"ok": True})


def normalize_bodyweight(bodyweight_unit, bodyweight):
    normalization_dict = {"p": 0.45, "l": 0.45, "k": 1, "g": 0.001, "s":  6.35}
    try:
        normalization_factor = normalization_dict[bodyweight_unit[0]]
    except KeyError:
        normalization_factor = 1
    return float(bodyweight) * normalization_factor


@app.route('/RegisterDrink/<drink>/<percentage>')
def register_drink(drink, percentage):
    global DRINK_UNITS
    DRINK_UNITS += calculate_drink_units(drink, percentage)
    extra_info = "."
    if DRINK_UNITS > WARNING_THREASHOLD:
        extra_info = "You shouldn't drink so much."
    if DRINK_UNITS > ULTRA_HANGOVER_WARNING_THREASHOLD:
        extra_info = "Warning! Last time you had this " \
                     "much you experienced a level {} " \
                     "hangover!.".format(ULTRA_HANGOVER_RATING)
    return jsonify({"ok": True, "extraInfo": extra_info})


def calculate_drink_units(drink, percentage):
    drink_dict = {"b": 500, "w": 200, "v": 50}
    try:
        drink_volume = drink_dict[drink[0]]
    except KeyError:
        drink_volume = 200
    return drink_volume * float(percentage)/1000


@app.route('/RequestBAC')
def request_bac():
    BACValue, BACError = calculate_bac()
    return jsonify({"ok": True, "BACValue": BACValue, "BACError": BACError})


def calculate_bac():
    BACValue = 0.806 * DRINK_UNITS * 1.2 / 0.58 / BODYWEIGHT
    BACError = 0.3 * BACValue
    return "{:2.2f}".format(BACValue), "{:2.2f}".format(BACError)
