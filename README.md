# baidu_fanyi
## Baidu translation API library

[![PyPI version](https://badge.fury.io/py/baidu-fanyi.svg)](https://badge.fury.io/py/baidu-fanyi)

Usage:

```
from baidu_fanyi import Translator

# create a Baidu developer account and project
# at http://developer.baidu.com/console#app/project
APP_ID = ""
SECRET_KEY = ""

tr = Translator(APP_ID, SECRET_KEY)

translation = tr.translate("auto", "yue", "hello, how are you doing?")

print(translation.text)
```

Error codes and language codes can be found ![here](https://fanyi-api.baidu.com/product/113)

Quick language codes for reference:

| Language            | Code |
| -                   | -    |
| Automatic           | auto |
| English             | en   |
| Chinese             | zh   |
| Traditional Chinese | cht  |
| Cantonese           | yue  |
| Classical Chinese   | wyw  |
| Japanese            | jp   |
| Korean              | kor  |
| French              | fra  |
| Spanish             | spa  |
| Thai                | th   |
| Arabic              | ara  |
| Russian             | ru   |
| Portuguese          | pt   |
| German              | de   |
| Italian             | it   |
| Greek               | el   |
| Dutch               | nl   |
| Polish              | pl   |
| Bulgarian           | bul  |
| Estonian            | est  |
| Danish              | dan  |
| Finnish             | fin  |
| Czech               | cs   |
| romanian            | rom  |
| Slovenian           | slo  |
| Swedish             | swe  |
| Hungarian           | hu   |
| Vietnamese          | vie  |
