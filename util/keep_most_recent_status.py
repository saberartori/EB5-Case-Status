import pandas as pd


def keep_most_recent_status(df_all_status):
    """
    Remove following status because it could show up after any status - will messed up the count
    For example, 'Document Was Mailed' could happened after fingerprint, case transferred, approval, and etc.
    """
    df_most_recent = df_all_status.copy()
    to_be_dropped = df_most_recent[(df_most_recent['Status'] == 'Card Was Returned To USCIS') |
                                   (df_most_recent['Status'] == 'Card Was Destroyed') |
                                   (df_most_recent['Status'] == 'Notice Returned') |
                                   (df_most_recent['Status'] == 'Document Was Mailed') |
                                   (df_most_recent['Status'] == 'Document Is Being Held For 180 Days') |
                                   (df_most_recent['Status'] == 'Duplicate Notice Was Mailed')
                                   ]
    df_recent = df_most_recent.drop(to_be_dropped.index)
    # Sort by date descending and keep most recent record
    df_recent['Date'] = pd.to_datetime(df_recent['Date'])
    df_recent = df_recent.sort_values(['CaseNum', 'Date'], ascending=[True, False])
    df_recent = df_recent.drop_duplicates(subset=['CaseNum'])

    return df_recent
