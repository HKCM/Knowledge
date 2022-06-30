import configparser

CONFIG_PATH = "./config.ini"
config = configparser.ConfigParser()
config.read(CONFIG_PATH,encoding='utf-8')
config_data = config['AAP']

block_headers = {
        'Authorization': config_data['accesstoken'],
        'content-type': 'application/json;charset=UTF-8',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
        'contenttype': 'application/json;charset=UTF-8',
        'sec-ch-ua-platform': '"macOS"',
        'origin': config_data['origin'],
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'user-agent': config_data['user-agent']
    }