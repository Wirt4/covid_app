'''imports'''
import pygeoip
import requests


class IP_Tracker:
    def __init__(self):
        ip_addr = requests.get("http://api.ipify.org/").text
        info = self._get_records(ip_addr)
        self.lat = info['latitude']
        self.lon = info['longitude']

    def _get_records(self, ip_addr):
        gip = pygeoip.GeoIP('GeoLiteCity.dat')
        result = gip.record_by_addr(ip_addr)
        return result
