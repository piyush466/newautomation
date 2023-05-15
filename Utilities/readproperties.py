import configparser
congi = configparser.RawConfigParser()
congi.read(r"C:\Users\Cliffex-Lead\frameworks demos\configuration\config.ini")

class ReadIni:

    @staticmethod
    def geturl():
        url =congi.get("common info", 'url')
        return url

    @staticmethod
    def getusername():
        user =congi.get("common info", 'username')
        return user

    @staticmethod
    def getpassword():
        pwd =congi.get("common info", 'password')
        return pwd
