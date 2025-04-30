import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\ankur\\PycharmProjects\\YTMusicApp\\configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationUrl():
        url = config.get('common info', 'baseurl')
        return url

    @staticmethod
    def getUsername():
        username = config.get('credential info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('credential info', 'password')
        return password

    @staticmethod
    def getVideoUrl():
        videoid = config.get('video info', 'video_id')
        videourl = ReadConfig.getApplicationUrl() + "watch?v=" + videoid
        return videourl