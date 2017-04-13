import logging
class Log():
    logging.basicConfig(filename="battleship.log", level=logging.INFO)
    def print_log(self,content):
        logging.info(content)


