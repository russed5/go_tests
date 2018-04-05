#!/usr/bin/python
# Author: russed5
# Revision: 1.0
# Code Reviewed by:
# Description: Testing the ability to execute VRO workflows via REST API
#
# Copyright (c) 2018 Dell Inc. or its subsidiaries.  All Rights Reserved.
# Dell EMC Confidential/Proprietary Information
#

import json
import os
import requests
import requests.exceptions


def test_service1_index():
    portnumber = ":8080"
    ipaddress = "10.0.2.15"
    apipath = "/"
    url = 'http://' + ipaddress + portnumber + apipath
    #headerstring = {"Content-Type": "application/json"}
    resp = requests.get(url, verify=False)
    respText = resp.text 
    print('xxxx', flowDetails)


    assert "Hello" in respText
    return None
