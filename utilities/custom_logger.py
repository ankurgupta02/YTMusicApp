import logging


class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        file_handler = logging.FileHandler("C:\\Users\\ankur\\PycharmProjects\\YTMusicApp\\logs\\automation.log",
                                           mode="w")
        format = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(format)
        logger.addHandler(file_handler)
        return logger