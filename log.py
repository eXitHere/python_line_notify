import logging

logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def err(msg):
    logging.error(msg.replace('\n', ' ').replace('\r', ''))

def info(msg):
    logging.info(msg.replace('\n', ' ').replace('\r', ''))