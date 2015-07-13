import requests

# Location to search for
q = "Yaba"

# Make a GET request to Google Geocode API to get information about that location
r = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=AIzaSyDWz0w-tYVP7iFwQ4qt2xR18UMuhm80mwk" % q)

# Raw JSON parsed as python dictionary or list as the case maybe
raw_json = r.json()

# Print out raw results
print "\nShowing Raw Results"
print "==================="
print raw_json
print "\n"

# Print out parsed results
print "Showing %s search results for %s" % ( len(raw_json['results']), q )
print "============================================="

for res in raw_json['results']:
  print "Where : %s" % res['formatted_address']
  print "Location: LNG %s LAT %s \n" % (res['geometry']['location']['lng'], res['geometry']['location']['lat'])