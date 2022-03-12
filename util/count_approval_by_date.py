import pandas as pd
from datetime import date


def count_approval_by_date(df_all_status, start_date, end_date=str(date.today())):
    df_all_status['Date'] = pd.to_datetime(df_all_status['Date'])

    ## Create a date range
    # range1 = pd.date_range('2020-10-01', periods=6, freq='M').astype(str).to_list()
    range_all = pd.date_range(start=start_date, end=end_date, freq='d').astype(str).to_list()
    # range1.extend(range2)

    ## Get the count
    count_list = []
    for i in range_all:
        temp = df_all_status[(df_all_status['Date'] <= i) & (df_all_status['Status_Short'] == '4-Approved')]
        temp = temp.drop_duplicates(subset=['CaseNum'])
        count = temp.shape[0]
        count_list.append(count)

    ## Make dataframe
    d = {'End_Date': range_all, 'Count': count_list}
    res = pd.DataFrame(d)
    res['Change'] = res['Count'].diff().fillna(0).astype(int)

    return res
