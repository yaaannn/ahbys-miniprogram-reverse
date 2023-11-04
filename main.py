import base64
import random

import requests
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1
from Crypto.PublicKey import RSA


class ahbys:
    def __init__(
        self, code: str, name: str, studentnum: str, idcode: str, college: str
    ) -> None:
        self.code = code
        self.name = name
        self.studentnum = studentnum
        self.idcode = idcode
        self.college = college
        self.gid = self.login()

    def __rsa_encrypt(self, message):
        key = RSA.importKey(
            "-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCa4KHNwDX44gGmmIAtRu4gjVYtGWZzcm4t+1wjUD4dn7fMLPvuK7ai4UrfDeEJE1RPwudJw+lJ6crql8wSIg7/DbTlG3ihsCT6dT9H5B9OoeR7K9VWUesaW/iyVL6HXiYOANabW14pvJATDmdq91Tfgp6PSQyvdfiRdV4r07crpQIDAQAB\n-----END PUBLIC KEY-----"
        )
        cipher_pkcs1_obj = Cipher_pkcs1.new(key)
        cipher_text = base64.b64encode(
            cipher_pkcs1_obj.encrypt(message.encode("utf-8"))
        )
        return str(cipher_text, encoding="utf-8")

    def login(self):
        url_login = "https://yun.ahbys.com/MiniAPI/10360/Graduate/login.ashx"

        params = {
            "rand": random.random(),
            "action": "binduser",
            "code": self.__rsa_encrypt(self.code),
            "name": self.__rsa_encrypt(self.name),
            "studentnum": self.__rsa_encrypt(self.studentnum),
            "idcode": self.__rsa_encrypt(self.idcode),
            "college": self.__rsa_encrypt(self.college),
        }

        res = requests.get(url_login, params=params)
        return res.json()["gid"]

    def get_base_info(self):
        url_base_info = (
            "https://yun.ahbys.com/MiniAPI/10360/Graduate/Dispatch/BaseInfo.ashx"
        )

        params = {
            "rand": random.random(),
            "action": "info",
            "gid": self.__rsa_encrypt(self.gid),
        }

        res = requests.get(url_base_info, params=params)
        return res.json()

    def get_link_info(self):
        url_link_info = (
            "https://yun.ahbys.com/MiniAPI/10360/Graduate/Dispatch/LinkInfo.ashx"
        )

        params = {
            "rand": random.random(),
            "action": "info",
            "code": self.code,
            "gid": self.__rsa_encrypt(self.gid),
        }

        res = requests.get(url_link_info, params=params)
        return res.json()

    def get_employer_info(self):
        url_employer_info = (
            "https://yun.ahbys.com/MiniAPI/10360/Graduate/Dispatch/EmployerInfo.ashx"
        )

        params = {
            "rand": random.random(),
            "action": "info",
            "code": self.code,
            "gid": self.__rsa_encrypt(self.gid),
        }

        res = requests.get(url_employer_info, params=params)
        return res.json()

    def get_archive_info(self):
        url_archive_info = (
            "https://yun.ahbys.com/MiniAPI/10360/Graduate/Dispatch/ArchiveInfo.ashx"
        )

        params = {
            "rand": random.random(),
            "action": "info",
            "code": self.code,
            "gid": self.__rsa_encrypt(self.gid),
        }

        res = requests.get(url_archive_info, params=params)
        return res.json()

    def get_chsi_api(self, year, ksh):
        url_chsi_api = (
            "https://yun.ahbys.com/MiniAPI/10360/Graduate/Dispatch/ChsiApi.ashx"
        )

        params = {
            "rand": random.random(),
            "action": "chsiinfo",
            "year": year,
            "code": self.code,
            "gid": self.gid,
            "ksh": ksh,
        }

        res = requests.get(url_chsi_api, params=params)
        return res.json()


if __name__ == "__main__":
    a = ahbys("00000", "张三", "000000000", "000000000000000000", "李四大学")

    print(a.get_employer_info())
