import json
import csv


def check(number):
    data = []
    path = "C:/Users/smoov/Downloads/analyses-20240505T132748Z-001/analyses/" + number + "/reports/report.json"
    with open (path, 'r') as file:
        data = json.load(file)
    filename = data['target']['file']['name']
    httpreqs = len(data['network']['http']) #HTTP requests
    dnsreqs = len(data['network']['dns']) #DNS connections
    tcpreqs = len(data['network']['tcp']) #TCP connections
    domains = len(data['network']['domains']) #domains reached
    behaviors = len(data['behavior']['generic']) #Behaviors Observed
    processes = len(data['behavior']['processtree']) #Processes Spawned
    # print(data['behavior']['processtree'])
    returner = [httpreqs, dnsreqs, tcpreqs, domains, processes, behaviors]
    return returner



def main():
    number = input("Pick a number 11-405: ")
    print (check(str(number)))

if __name__ == "__main__":
    main()