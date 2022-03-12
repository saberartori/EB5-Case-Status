#!/usr/bin/env python
# coding: utf-8

# For issue 'SSL: CERTIFICATE_VERIFY_FAILED with urllib'
# There is command line program that you can run on MacOsX that will install the certificates:
# sudo /Applications/Python\ 3.X/Install\ Certificates.command
# The sudo command will prompt for you password to elevate your privileges.

import pandas as pd
import os
from datetime import datetime
from util.get_online_status import get_online_status

pd.options.mode.chained_assignment = None  # default='warn'

## Input this part
FY_YEAR = 2022

CaseNum_Start = 2290057668
CaseNum_Ended = 2290059999

exclude_CardDelivered = True
exclude_NewCard = True

## Default Parma
caseNum_list = list(range(CaseNum_Start, CaseNum_Ended + 1))
dt = datetime.now().strftime("%Y%m%d-%H%M%S")

if __name__ == '__main__':
    path = f"FY{FY_YEAR}_485"
    if not os.path.exists(path):
        # Create a new directory because it does not exist
        os.makedirs(path)

    ## Get all status from USCIS
    try:
        df = get_online_status(caseNum_list, dt)
    except Exception as e:
        print(e)
    else:
        # Save a copy of result
        df.to_csv(path + "/FY{}-485-Status_{}_{}_{}.csv".format(FY_YEAR, CaseNum_Start, CaseNum_Ended, dt), index=False)

        # Option to exclude below two status for new case numbers because don't know which card (i.e. no form type info)
        if exclude_CardDelivered:
            df = df[df['Status'] != 'Card Was Delivered']
        if exclude_NewCard:
            df = df[df['Status'] != 'New Card Is Being Produced']

        # Save as csv
        df.to_csv(path + "/FY{}-485-Status_{}_{}_{}.csv".format(FY_YEAR, CaseNum_Start, CaseNum_Ended, dt), index=False)
