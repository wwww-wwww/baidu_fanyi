import random, hashlib, urllib
from requests import Session
from urllib.parse import urljoin

API_URL = "https://api.fanyi.baidu.com/api/trans/vip/translate"

class TranslationException(Exception):
  def __init__(self, result):
    self.error_code = int(result["error_code"])
    self.message = result["error_msg"]
    super().__init__("{}: {}".format(self.error_code, self.message))

class Translation():
  def __init__(self, result):
    self.__dict__ = result
    self.text = "".join([res["dst"] for res in self.trans_result])

class Translator():
  def __init__(self, appid, secret_key):
    self.appid = appid
    self.secret_key = secret_key
    self.session = Session()

  def translate(self, from_lang, to_lang, query_text):
    url = self.get_url(from_lang, to_lang, query_text)
    with self.session.get(url) as r:
      result = r.json()
      if "error_code" in result:
        raise TranslationException(result)
      return Translation(result)

  def get_url(self, from_lang, to_lang, query_text):
    salt = random.randint(32768, 65536)
    sign = "".join([self.appid, query_text, str(salt), self.secret_key])
    m1 = hashlib.md5()
    m1.update(sign.encode("utf-8"))
    sign = m1.hexdigest()
    
    params = {
      "appid": self.appid,
      "q": urllib.parse.quote(query_text),
      "from": from_lang,
      "to": to_lang,
      "salt": salt,
      "sign": sign
    }

    params = ["{}={}".format(key, params[key]) for key in params]
    return "{}?{}".format(API_URL, "&".join(params))
