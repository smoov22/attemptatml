import json
import csv


def check(number):
    data = []
    path = "C:/Users/smoov/Downloads/analyses-20240505T132748Z-001/analyses/" + number + "/reports/report.json"
    with open (path, 'r') as file:
        data = json.load(file)
    filename = data['target']['file']['name']
    httpreqs = len(data['network']['http'])
    dnsreqs = len(data['network']['dns'])
    print(data['network']['dns'])
    print(dnsreqs)
    print(httpreqs)
    return filename



def main():
    number = input("Pick a number 11-405: ")
    print (check(number))

main()