import logging

class Logge:

    @staticmethod
    def loggen():
        logger  = logging.getLogger(__name__)
        filehandle = logging.FileHandler(r"C:\Users\Cliffex-Lead\frameworks demos\Logs\Logs.log")
        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(message)s")

        filehandle.setFormatter(formatter)
        logger.addHandler(filehandle)
        logger.setLevel(logging.INFO)
        logger.setLevel(logging.DEBUG)
        return logger
