import pickle
import pandas as pd
from util.short_label import short_label
from util.get_case_info import get_case_info
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

status_rename_map = pickle.load(open('util/status_mappings.p', 'rb'))


def get_online_status(caseNum_list, current_timestamp):
    ## Get Data through Multi-Thread
    with ThreadPoolExecutor(max_workers=None) as executor:
        futures = []
        all_data_list = []
        for caseNum in caseNum_list:
            futures.append(executor.submit(get_case_info, caseNum))
        for future in tqdm(as_completed(futures)):
            if len(future.result()) > 0:
                # print('future result:', future.result())
                # print('length: ', len(future.result()))
                all_data_list.append(future.result())
            else:
                pass
    """
    Sometime can get multi-result at the same time
    Separate it to multi-list and append one by one
    """
    all_data = []
    for i in range(len(all_data_list)):
        if len(all_data_list[i]) > 4:
            to_split = all_data_list[i]
            temp = [to_split[4 * i: 4 * (i + 1)] for i in range(int(len(to_split) / 4))]
            for j in range(len(temp)):
                all_data.append(temp[j])
        else:
            all_data.append(all_data_list[i])

    ## Generate dataframe
    if len(all_data) == 0:
        raise ValueError('*No any case we want in this Case Number List')
    else:
        df = pd.DataFrame(all_data, columns=['CaseNum', 'Status', 'Date', 'Desc'])
        df = df.drop_duplicates(subset=['CaseNum', 'Status'])

        ## Add and Format columns
        df['Generated_at'] = current_timestamp
        df['Status'] = df['Status'].replace(status_rename_map)
        df['Status_Short'] = df.apply(lambda row: short_label(row), axis=1)

        ## Final re-org columns
        df = df[['CaseNum', 'Status_Short', 'Date', 'Status', 'Generated_at', 'Desc']]

    return df
