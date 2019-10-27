# -*- coding: utf-8 -*-
"""The app module, containing the app factory function, is used to serve as fake camera"""

from flask import request, Blueprint
from PIL import Image
import time, math, os
from webviewer.photos.models import Photo
from motors.models import Motors
from webviewer.extensions import (db)

import json

blueprint = Blueprint('motors', __name__, url_prefix="/motors", static_folder="static", static_url_path='/motors/static')


@blueprint.route('/set', methods=['POST'])
def set_motors():
    action = request.args.get('action', '')
    action_para = request.args.get('parameters', '')

    print("action=%s, parameters=%s"%(action, action_para))

    if action == "open":
        # TO DO: open the motors
        return "motors are opened", 200

    if action == "close":
        # TO DO: close the motors
        return "motors are closed", 200


    if action == "setPara":
        para_dict = json.loads(action_para)
        print(para_dict)


        motors = Motors.query.first()
        motors.x = para_dict["x"]
        motors.y = para_dict["y"]

        # TODO : More parameters
        db.session.commit()

        motor_para = {"x": motors.x,
                      "y": motors.y}

        return "Camera parameres as %s "% json.dumps(motor_para), 200

    if action == "getPara":
        motors = Motors.query.first()
        if motors is None:
            moto = Motors()
            db.session.add(moto)
            db.session.commit()
            motors = Motors.query.first()


        motors_para = {"x": motors.x,
                       "y": motors.y,
                       "z": motors.z}

        return json.dumps(motors_para), 200



    if action == "enableMotor":
        action_para = request.args.get('parameters', '')

        if action_para =='x':
            pass

        if action_para == 'y':
            pass

        if action_para == 'z':
            pass

        if action_para == 'all':
            pass

        return "Enabled axis %s"%action_para, 200


    if action == "disableMotor":
        action_para = request.args.get('parameters', '')

        if action_para =='x':
            pass

        if action_para == 'y':
            pass

        if action_para == 'z':
            pass

        if action_para == 'all':
            pass

        return "Disabled axis %s"%action_para, 200

    if action == "goto":
        action_para = request.args.get('parameters', '')

        para_dict = json.loads(action_para)
        axis = para_dict["axis"]
        target = para_dict["target"]
        speed =  para_dict["speed"]
        # TODO: Call motors togo postion
        return "going to target %d, axis %s"% (target, axis), 200


    if action == "move":
        action_para = request.args.get('parameters', '')
        para_dict = json.loads(action_para)
        axis = para_dict["axis"]
        target = para_dict["target"]
        speed =  para_dict["speed"]
        # TODO: Call motors togo postion
        return "going to target %d, axis %s"% (target, axis), 200

    if action == "stop":
        action_para = request.args.get('parameters', '')
        para_dict = json.loads(action_para)
        axis = para_dict["axis"]
        target = para_dict["target"]
        speed =  para_dict["speed"]
        # TODO: Call motors togo postion
        return "going to target %d, axis %s"% (target, axis), 200

    if action == "checkPocsition":
        motors = Motors.query.first()
        motors_para = {"x": motors.x,
                       "y": motors.y,
                       "z": motors.z}

        return json.dumps(motors_para), 200


    if action == "checkOnTarget":
        action_para = request.args.get('parameters', '')
        para_dict = json.loads(action_para)
        axis = para_dict["axis"]
        target = para_dict["target"]
        speed = para_dict["speed"]
        # TODO: Call motors togo postion
        return "going to target %d, axis %s" % (target, axis), 200


    return "Unknown action", 200


