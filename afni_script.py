#!/bin/python

############################################################################
# Copyright [2019] [Khorgolkhuu Odbadrakh and Lonnie D. Crosby]
# 
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
# 
#       http://www.apache.org/licenses/LICENSE-2.0
# 
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
############################################################################

from pyspark import SparkContext
import os, sys

def fnames():
        path = os.getcwd()
        names = list(filter(lambda x: x.startswith('proc.FT'), os.listdir('.')))
        filenames = [os.path.join(path,s) for s in names]
        return filenames

def afni(x):
        scriptfile = os.path.basename(x)
        outdir = scriptfile[5:]
        pathname = os.path.dirname(x) 
        sourcedir = os.path.join(pathname,outdir)
        os.system('ln -s ' + sourcedir + ' .')
	os.system('tcsh -xef ' + x + ' 2>&1 | tee output.' + os.path.basename(x))

##################################################
def main():
        sc = SparkContext(appName='afni_app')
        files = fnames()
        afni_rdd = sc.parallelize(files,8)
        afni_rdd.foreach(afni)

##################################################
if __name__ == '__main__':
        main()

