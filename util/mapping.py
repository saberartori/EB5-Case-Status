import pickle

rename_mappings = {
    'Card Was Delivered To Me By The Post Office': 'Card Was Delivered',
    'Case Was Transferred And A New Office Has Jurisdiction': 'Case Was Transferred',
    'Case Transferred To Another Office': 'Case Was Transferred',
    'Case Transferred And New Office Has Jurisdiction': 'Case Was Transferred',
    'Case Was Updated To Show Fingerprints Were Taken': 'Fingerprints Taken',
    'Case Was Transferred To Schedule An Interview': 'Interview Was Ready',
    'Case is Ready to Be Scheduled for An Interview': 'Interview Was Ready',
    'Interview Was Completed And My Case Must Be Reviewed': 'Interview Was Completed',
    'Interview Cancelled And Notice Ordered': 'Interview Was Cancelled',
    'Case Was Updated To Show That No One Appeared for In-Person Processing': 'Interview Was NoShow',

    'Request for Initial Evidence Was Sent': 'RFE Sent',
    'Request for Additional Evidence Was Sent': 'RFE Sent',
    "Response To USCIS' Request For Evidence Was Received": 'RFE Responded',
    'Correspondence Was Received And USCIS Is Reviewing It': 'RFE Responded',
    'Correspondence Was Received': 'RFE Responded',
    'Continuation Notice Was Mailed': 'RFE Responded',

    'Case Rejected Because I Sent An Incorrect Fee': 'Rejected-Incorrect Fee',
    'Case Rejected Because The Version Of The Form I Sent Is No Longer Accepted': 'Rejected-Old Version',
    'Case Was Rejected Because I Did Not Sign My Form': 'Rejected-No Signature',
    'Case Was Rejected Because It Was Improperly Filed': 'Rejected-Improperly Filed',
    'Petition/Application Was Rejected For Insufficient Funds': 'Rejected-Insufficient Funds',
    'Case Rejected For Form Not Signed And Incorrect Form Version': 'Rejected-NoSign and OldVersion',
    'Case Rejected For Incorrect Fee, Payment Not Signed And Incorrect Form Version': 'Rejected-Incorrect Fee and OldVersion',
    'Case Rejected For Incorrect Fee And Form Not Signed': 'Rejected-Incorrect Fee and NoSign',

    'Withdrawal Acknowledgement Notice Was Sent': 'Withdrawal Acknowledged',
    'Notice Was Returned To USCIS Because The Post Office Could Not Deliver It': 'Notice Returned',
    'Document Was Returned To USCIS': 'Notice Returned',
    'Document Is Being Held For 180 Days': 'Notice Returned'
}

pickle.dump(rename_mappings, open('status_mappings.p', 'wb'))
