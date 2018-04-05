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
    portnumber = ":30002"
    ipaddress = "192.168.99.100"
    apipath = "/"
    url = 'http://' + ipaddress + portnumber + apipath
    #headerstring = {"Content-Type": "application/json"}
    resp = requests.get(url, verify=False)
    respText = resp.text 

    assert "Hello" in respText
    return None
