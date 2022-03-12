def short_label(row):
    if (row['Status'] == 'Case Was Received') | \
            (row['Status'] == 'Case Was Transferred') | \
            (row['Status'] == 'Fingerprint Fee Was Received'):
        current_status = '0-Received'
    elif row['Status'] == 'Fingerprints Taken':
        current_status = '1-Fingerprint-taken'
    elif row['Status'][:3] == 'RFE':
        current_status = '2a-RFE'
    elif row['Status'][:16] == 'Expedite Request':
        current_status = '2b-Expedite'
    elif (row['Status'] == 'Date of Birth Was Updated') | (row['Status'] == 'Name Was Updated'):
        current_status = '2c-UpdateInfo'
    elif (row['Status'] == 'Fee Will Be Refunded') | (row['Status'] == 'Fee Refund Was Mailed') | \
            (row['Status'] == 'Case Was Reopened'):
        current_status = '2z-Misc'
    elif row['Status'][:13] == 'Interview Was':
        current_status = '3-Interview'
    elif (row['Status'] == 'Card Was Delivered') | \
            (row['Status'] == 'Card Was Mailed To Me') | \
            (row['Status'] == 'Case Was Approved') | \
            (row['Status'] == 'New Card Is Being Produced'):
        current_status = '4-Approved'
    elif row['Status'] == 'Case Was Denied':
        current_status = '4-Denied'
    elif (row['Status'] == 'Withdrawal Acknowledged') | (
            row['Status'] == 'Case Closed Benefit Received By Other Means'):
        current_status = '7-Withdrawn'
    elif row['Status'][:8] == 'Rejected':
        current_status = '8-Rejected'
    else:
        current_status = '9-Others'
    return current_status
