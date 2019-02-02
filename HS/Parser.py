from pathlib import Path
import zipfile
from kafka import KafkaProducer
import argparse
import json
from jsonschema import validate



def parser(data, objname = None, previous_output = None):
    games = ['range_start','range_end']
    card_history = ['user_hash','added']
    card = ['user_hash','added','player','card_counter']
    output = {}
    card_counter = 0    
    for items in data:
        if objname:
            for key in eval(objname):
                output[key] = previous_output[key]
            if 'card_counter' not in eval(objname):
                output['card_counter'] = card_counter
                card_counter+=1
        if type(data) == dict:
            items = items.encode('ascii')
            if type(data[items]) not in [list,dict]:
                output[items] = str(data[items]).encode('ascii')
            else:
                parser(data[items], items, output)
        elif type(data) == list:
            for item in items:
                item = item.encode('ascii')
                if type(items[item]) not in [list,dict]:
                    output[item] = str(items[item]).encode('ascii')
                else:
                    parser(items[item], item, output)
            print output
    if type(data) == dict:
        print output
                        
    

def main():
    #parser = argparse.ArgumentParser(description='Rides events aggregate.')

    #parser.add_argument('-t', '--topic', metavar='<topic>', type=str,
    #                    required=True,
    #                    help='Kafka topic name.')

    #parser.add_argument('-K', '--kafka_host', metavar='<host>', type=str,
    #                    required=True,
    #                    help='Kafka host list.')

    #args = parser.parse_args()

    #topic = args.topic
    #host = args.kafka_host
    
    #producer = KafkaProducer(bootstrap_servers=host)
    
    #while True:
    zippath = Path('/home/eduardo/personal_git/HS_samples/Extract/HearthScry/').glob('**/*.zip')
    zips = [x for x in zippath]
    for z in zips:
        filedir = str(z).replace('.zip','')
        with zipfile.ZipFile(str(z), 'r') as zip_ref:
            zip_ref.extractall(filedir)
        filepath = Path(filedir).glob('**/*.json')
        files = [x for x in filepath]
        for f in files:
            with open(str(f)) as jsonfile:
                data = json.load(jsonfile)
        with open('/home/eduardo/personal_git/HS_samples/HS/hearthscryschema.json') as schemafile:
                schema = json.load(schemafile)
        try:
            validate(data,schema)
        except Exception as e:
            print 'error'
        parser(data)

        

        #for finfo in zipped.infolist():
        #    ifile = zipped.open(finfo)
        #    line_list = ifile.readlines()
        #    print line_list

        #message = raw_input("Input message:")
        #response = producer.send(topic, message)
        #print response

if __name__ == "__main__":
    main()
