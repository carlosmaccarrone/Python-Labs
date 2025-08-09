"""
IP Geolocation Lookup using PyGeoIP.

This script uses the pygeoip library and a local GeoLiteCity.dat database file
to obtain geographical information (city, region, country, latitude, longitude)
based on an IP address.

Requirements:
- pygeoip library (`pip install pygeoip`)
- GeoLiteCity.dat database file from MaxMind (https://dev.maxmind.com/geoip/legacy/geolite/)
  Download and place it at '/usr/share/GeoIP/GeoLiteCity.dat' or modify the path below.

Usage:
- Change the target IP address by modifying the `target_ip` variable.
- Run the script to print the geolocation data of the IP.

Note:
- This script is designed for Python 3. If you have Python 2, minor modifications may be necessary.
- The accuracy of geolocation depends on the database version.
"""

import pygeoip

def print_geolocation(ip_address):
    """
    Print geolocation info for a given IP address.

    Args:
        ip_address (str): The IP address to geolocate.

    Prints city, region, country, latitude, and longitude.
    """
    geo_db_path = '/usr/share/GeoIP/GeoLiteCity.dat'
    gi = pygeoip.GeoIP(geo_db_path)

    record = gi.record_by_name(ip_address)
    if not record:
        print(f"[!] No geolocation data found for IP: {ip_address}")
        return

    city = record.get('city', 'N/A')
    region = record.get('region_code', 'N/A')
    country = record.get('country_code3', 'N/A')
    latitude = record.get('latitude', 'N/A')
    longitude = record.get('longitude', 'N/A')

    print(f"[*] Target IP: {ip_address} - Geo-location found:")
    print(f"[+] City: {city}, Region: {region}, Country: {country}")
    print(f"[+] Latitude: {latitude}, Longitude: {longitude}")

if __name__ == '__main__':
    target_ip = '110.8.88.36'
    print_geolocation(target_ip)