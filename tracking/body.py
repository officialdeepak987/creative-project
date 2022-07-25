import phonenumbers
from text import number
from phonenumbers import geocoder
ch_number =phonenumbers.parse(number,"CH") # ch stand for country history
print(geocoder.description_for_number(ch_number,"en"))#en means english you want the information to display in english
# how to track the number of network provider
from phonenumbers import carrier
service_provider=phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_provider,"en"))
