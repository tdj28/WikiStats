#!/usr/bin/python 

import sys
import datetime

with open(sys.argv[1]) as f:
    content = f.readlines()
    
monthinteger = int(sys.argv[1].split('/')[0][-2:])

month = datetime.date(1900, monthinteger, 1).strftime('%b')
filename = "{}.sql".format(month)
ff = open(filename,'w')

ff.write("use wikistats;\n")
ff.write("CREATE TABLE {0}(id INT NOT NULL AUTO_INCREMENT, word VARCHAR(64) NOT NULL, count VARCHAR(64) NOT NULL, primary key(id)) ENGINE=MyISAM;\n".format(month))

for i in content:
    word = i.strip().split()[0].replace('\"','').replace('\'','')
    count = i.strip().split()[1]
    ff.write("INSERT INTO {0} VALUES('', '{1}', {2});\n".format(month, word, count))
    
ff.close()
