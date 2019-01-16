#!/usr/bin/env python2.7

try:
    import simplejson as json
except ImportError:
    import json
import urllib2
import base64
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", help="Hostname or IP of APEX",
                        required=True)
    parser.add_argument("--user", help="Apex Username", default="Admin")
    parser.add_argument("--password", help="Apex Password", default="1234")
    parser.add_argument("--ptype", help="inputs or outputs", default="inputs")
    parser.add_argument("--type", help="Type of device", default="Temp")
    args = parser.parse_args()
    return args


def read_apex(jdata, type="Temp", ptype="inputs"):
    data = { "data": [] }

    if ptype == 'inputs':
        for idx,input in enumerate(jdata['istat']['inputs']):
            nd = {
                '{#PKEY}' : 'inputs',
                '{#INDEX}' : idx,
                '{#DID}' : input['did'],
                '{#TYPE}' : input['type'],
                '{#NAME}' : input['name'],
            }
            if type == input['type']:
                data['data'].append(nd)

    if ptype == 'outputs':
        for idx,input in enumerate(jdata['istat']['outputs']):
            nd = {
                '{#PKEY}' : 'outputs',
                '{#INDEX}' : idx,
                '{#DID}' : input['did'],
                '{#TYPE}' : input['type'],
                '{#NAME}' : input['name'],
            }
            if type == input['type']:
                data['data'].append(nd)

    print(json.dumps(data))


def main():
    args = parse_arguments()
    
    request = urllib2.Request('http://' + args.host + '/cgi-bin/status.json')
    base64string = base64.encodestring('%s:%s' % (args.user, args.password)).replace('\n', '')
    request.add_header("Authorization", "Basic %s" % base64string)   
    content = urllib2.urlopen(request)
    jdata = json.load(content)

    read_apex(jdata, args.type, args.ptype)


if __name__ == "__main__":
    main()
