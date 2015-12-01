import urllib.parse, urllib.request
import webbrowser
import json

geocode_base_url = 'https://maps.googleapis.com/maps/api/geocode/json'
streetview_base_url = 'https://maps.googleapis.com/maps/api/streetview'

def get_image(lat, lng, width=600, height=300):
    
    params = urllib.parse.urlencode([('size', '%dx%d' % (width, height)), 
                                     ('location', '%f,%f' % (lat, lng))])
    url = streetview_base_url + '?' + params
    webbrowser.open(url)


def get_location(address):
    params = urllib.parse.urlencode([('address', address)])
    url = geocode_base_url + '?' + params
    response = urllib.request.urlopen(url).readall().decode('utf-8')
    result = json.loads(response)
    for s in result['results']:
        location = s['geometry']['location']
        return (location['lat'], location['lng'])

address = input("Enter your address: ")
(lat, lng) = get_location(address)
get_image(lat, lng)








