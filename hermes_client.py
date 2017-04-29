import requests

host = 'http://0.0.0.0:8080'


def g(action, *args):
    url = host+'/'+action
    for arg in args:
        url += '/'+str(arg)
    r = requests.get(url)
    return r.json()


def Hermes___init__():
    return g('Hermes___init__', )['return_value']


def Hermes_connect():
    return g('Hermes_connect', )['return_value']


def Hermes_disconnect():
    return g('Hermes_disconnect', )['return_value']


def Hermes_move(speed, turn):
    return g('Hermes_move', speed, turn)['return_value']


def Hermes_change_posture(posture_type):
    return g('Hermes_change_posture', posture_type)['return_value']


def Hermes_jump(jump_type):
    return g('Hermes_jump', jump_type)['return_value']


def Hermes_jump_load():
    return g('Hermes_jump_load', )['return_value']


def Hermes_jump_cancel():
    return g('Hermes_jump_cancel', )['return_value']


def Hermes_jump_stop():
    return g('Hermes_jump_stop', )['return_value']


def Hermes_simple_animation(animation_type):
    return g('Hermes_simple_animation', animation_type)['return_value']


def Hermes_stop():
    return g('Hermes_stop', )['return_value']


if __name__ == '__main__':
    pass
