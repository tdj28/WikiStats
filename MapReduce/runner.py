#!/usr/bin/python

import os
#for i in `ls /recent/2011/OCT/`; do aws s3api put-object --bucket wikidatajones --key pagecounts2011/OCT/$i --body /recent/2011/OCT/$i; done        


#http://dumps.wikimedia.org/other/pagecounts-raw/2007/2007-12/



#wget -r -np -nd -l 1 -A gz http://dumps.wikimedia.org/other/pagecounts-raw/2012/2012-10/index.html
# python WikiMRjob.py -r emr s3://wikidatajones/monthly/200712" --output-dir=s3://wikidatajones/recession/200712" --emr-job-flow-id=j-A7WOS2ZU66GX

flow_id = "j-A7WOS2ZU66GX"
year = 2008
month = 1
while year < 2009:
    while month < 13:
        if len(str(month))==1:
            i = "0" + str(month)
        else:
            i = str(month)
        source_folder = str(year) + i 
        destination_folder = "recession/" + str(year) + i
        # --cmdenv could be useful elsewhere
        cmd = "python WikiMRjob.py -r emr s3://wikidatajones/monthly/"+source_folder+"/ --output-dir=s3://wikidatajones/" + destination_folder + "/ --emr-job-flow-id=" + flow_id
        os.system(cmd)
        print cmd
        month += 1
    month = 1
    year += 1