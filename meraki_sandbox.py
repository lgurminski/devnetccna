#!/bin/python3

from meraki_sdk.meraki_sdk_client import MerakiSdkClient
import meraki

API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'

if True:
    MERAKI = MerakiSdkClient(API_KEY)
    ORGs = MERAKI.organizations.get_organizations()

    PARAMS = {}
    PARAMS["organization_id"]="549236"
    NETs = MERAKI.networks.get_organization_networks(PARAMS)

    for org in ORGs:
        print("Org ID: {} and Org name: {}".format(org['id'],org['name']))

    for net in NETs:
        print(net['id'], net['name'], net['tags'])

if True:
    dashboard = meraki.DashboardAPI(API_KEY)
    ORGs = dashboard.organizations.getOrganizations()
    for org in ORGs:
        print("Org ID: {} and Org name: {}".format(org['id'],org['name']))
        
