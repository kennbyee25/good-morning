import time
import yeelight
import json

def load_config():
    with open('config/config.json') as f:
        return json.load(f)

if __name__ == '__main__':
    config = load_config()
    bulb_ip = config['bulb_ip']
    start_temp = config['start_temp']
    end_temp = config['end_temp']
    duration = config['duration']
    steps = config['steps']

    bulb = yeelight.Bulb(bulb_ip)
    properties = bulb.get_properties()
    bulb_is_on = properties['power'] == 'on'

    if not bulb_is_on:
        bulb.turn_on()
        bulb.set_color_temp(start_temp)
        bulb.set_brightness(1)
    
    for i in range(steps+1):
        temp = start_temp + (end_temp - start_temp) * i / steps
        brightness = int(100 * i / steps)
        bulb.set_color_temp(temp)
        bulb.set_brightness(brightness)
        
        time.sleep(duration / steps)
