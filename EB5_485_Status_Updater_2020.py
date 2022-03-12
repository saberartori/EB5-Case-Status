#!/usr/bin/env python
# coding: utf-8

# For issue 'SSL: CERTIFICATE_VERIFY_FAILED with urllib'
# There is command line program that you can run on MacOsX that will install the certificates:
# sudo /Applications/Python\ 3.X/Install\ Certificates.command
# The sudo command will prompt for you password to elevate your privileges.

import pandas as pd
from datetime import datetime
from pytz import timezone
from util.get_online_status import get_online_status
from util.keep_most_recent_status import keep_most_recent_status
from util.count_approval_by_date import count_approval_by_date

pd.options.mode.chained_assignment = None  # default='warn'

FY_YEAR = 2020
dt = datetime.now(timezone('US/Eastern')).strftime("%Y%m%d-%H%M%S")  # Default ET

if __name__ == '__main__':
    ## Read CSV
    df_all = pd.read_csv(f"FY{FY_YEAR}/CaseNum-all_status.csv")
    df_all['CaseNum'] = df_all['CaseNum'].astype(str)

    ## Default Parma
    caseNum_list = df_all.CaseNum.unique().tolist()

    ## Get all status from USCIS
    df_new_status = get_online_status(caseNum_list, dt)

    ## Append the new dataframe, sort and DeDup - Save as csv
    df = pd.concat([df_all, df_new_status])
    df = df.sort_values(['CaseNum', 'Generated_at'])
    df = df.drop_duplicates(subset=['CaseNum', 'Status'])
    df.to_csv(f"FY{FY_YEAR}/CaseNum-all_status.csv", index=False)

    ## Check how many are updated
    df_updated_new = df[df['Generated_at'] == dt]
    update_num = len(df_updated_new.index)

    if update_num > 0:
        print('{} cases have been updated today'.format(update_num))
        print(df_updated_new[['CaseNum', 'Status', 'Date', 'Generated_at']])
        df_updated_new_formatted = df_updated_new[['CaseNum', 'Status', 'Date', 'Generated_at', 'Status_Short']]

        try:
            df_updated_log = pd.read_csv(f"FY{FY_YEAR}/Update_log.csv")
        except FileNotFoundError as e:
            df_updated_all = df_updated_new_formatted
        else:
            df_updated_log['CaseNum'] = df_updated_log['CaseNum'].astype(str)
            df_updated_all = pd.concat([df_updated_log, df_updated_new_formatted])

        df_updated_all.to_csv(f"FY{FY_YEAR}/Update_log.csv", index=False)
    else:
        print('No Case is updated today...')

    ## Another file to keep most recent
    df_recent = keep_most_recent_status(df)
    df_recent.to_csv(f"FY{FY_YEAR}/CaseNum-most_recent_status.csv", index=False)

    ## Count approval
    df_count = count_approval_by_date(df, start_date='2021-10-01')
    df_count.to_csv(f"FY{FY_YEAR}/Approval_count_by_date.csv", index=False)
