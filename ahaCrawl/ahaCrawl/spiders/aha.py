import json
import requests
import scrapy


class ExampleItem(scrapy.Item):
    response_data = scrapy.Field()

class ExampleSpider(scrapy.Spider):
    name = "aha"

    def start_requests(self):
        url = "https://rest-prod-aha.evergent.com/aha/getOAuthAccessTokenv2"
        payload = json.dumps({
            "GetOAuthAccessTokenv2RequestMessage": {
                "contactUserName": "honey.acc24@gmail.com",
                "contactPassword": "Marvel@1234",
                "deviceMessage": {
                    "deviceName": "web",
                    "deviceType": "mobile-web",
                    "modelNo": "firefox",
                    "serialNo": "081bd8e1-c46d-4ab3-bdef-1c1ef022718c",
                    "appType": "Web"
                },
                "channelPartnerID": "ARHAMEDIA",
                "apiUser": "ahaapiuser",
                "apiPassword": "Aha@p!u$#r123#$"
            }
        })
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-type': 'application/json',
            'Origin': 'https://www.aha.video',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Referer': 'https://www.aha.video/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'TE': 'trailers'
        }

        yield scrapy.Request(url=url, method='POST', body=payload, headers=headers, callback=self.parse)

    def parse(self, response):
        response_data = json.loads(response.text)
        item = ExampleItem()
        item['response_data'] = response_data
        yield item
