"""turns zip codes to a range of latitudes and longitudes"""
from geopy.geocoders import Nominatim
from ip_tracker import IP_Tracker

class GeoLocator:
    #lower lat bound, upper lat bound, lower lon bound, higher lon bound
    _lat_lon_bounds = []

    def convert_zip_code(self, zip_code):
        """returns a bounding box of lower lat bound, higher lat bound,"""
     # instantiate a new Nominatim client
        app = Nominatim(user_agent="zip_code_converter")
        location = app.geocode(zip_code).raw
        self._lat_lon_bounds = self._convert_box(location['boundingbox'])

    def county_no_parameters(self):
        ipt = IP_Tracker()
        res = []
        app = Nominatim(user_agent="zip_code_converter")
        ##empty query should return closest match to ip address of user
        res_dict = app.reverse((ipt.lat, ipt.lon)).raw['address']
        res.append(res_dict['state'])
        res.append(res_dict['county'])
        return res



    def get_bounds(self):
        return self._lat_lon_bounds

    def _convert_box(self, bbox):
        bb =[]
        for i in bbox:
            bb.append(float(i))
        return bb

