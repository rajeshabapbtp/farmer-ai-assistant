import geocoder

def get_location():
    g = geocoder.ip('me')

    if g.ok:
        city = g.city
        country = g.country
        return city, country
    
    return None, None