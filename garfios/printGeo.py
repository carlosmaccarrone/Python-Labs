import pygeoip
gi = pygeoip.GeoIP('/usr/share/GeoIP/GeoLiteCity.dat')

def imprimirPosicion(tgt):
	rec = gi.record_by_name(tgt)
	city = rec['city']
	region = rec['region_code']
	country = rec['country_code3']
	long = rec['longitude']
	lat = rec['latitude']
	print '[*] Target: ' + tgt + ' Geo-localizado. '
	print '[+] '+str(city)+', '+str(region)+', '+str(country)
	print '[+] Latitud: '+str(lat)+ ', Longitud: '+ str(long)

tgt = '110.8.88.36'
imprimirPosicion(tgt)

# pip install pygeoip
# wget -N http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz
# gunzip GeoLiteCity.dat.gz
# mv GeoLiteCity.dat /usr/share/GeoIP/

# Ejemplo:
# 	{
# 	    'city': u'Mountain View',
# 	    'region_code': u'CA',
# 	    'area_code': 650,
# 	    'time_zone': 'America/Los_Angeles',
# 	    'dma_code': 807,
# 	    'metro_code': 'San Francisco, CA',
# 	    'country_code3': 'USA',
# 	    'latitude': 37.41919999999999,
# 	    'postal_code': u'94043',
# 	    'longitude': -122.0574,
# 	    'country_code': 'US',
# 	    'country_name': 'United States',
# 	    'continent': 'NA'
# 	}

