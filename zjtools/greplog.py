#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import re

parms = sys.argv
R6_OSC_LOG_DIR = r'/var/log/s3/servicelog/osc/'
OSC_REQ = re.compile(r'^\[[0-9A-Z]+\]')

def get_acc_log(log_dir):
    sh_cmd = 'grep ' + parms[1] + ' ' + log_dir + 'obs.access.log*' # grep xx /var/log/s3/servicelog/osc/obs.access.log*
    try:
        return os.popen(sh_cmd).read().split('\n')
    except:
        return []

def cal_osc_log(log_file):
    result = []
    is_content = 0
    for ln in open(log_file):
        flag1 = 1 if OSC_REQ.match(ln) else 0
        if flag1 == 1:
            if parms[1] in ln:
                flag1 += 1
                is_content = 1
            else:
                is_content = 0
        if flag1 == 2 or is_content == 1:
            result.append(ln)
    return result

def show_list(lst):
    for lt in lst:
        if isinstance(lt, list):
            show_list(lt)
        else:
            lt = lt[:-1] if lt.endswith('\n') else lt
            if lt:
                print(lt)

def get_osc_log(log_dir):
    get_log_file_cmd = 'grep ' + parms[1] + ' ' + log_dir + "obs.osc.log* | awk -F ':' '{print $1}' | sort | uniq"
    try:
        log_file = os.popen(get_log_file_cmd).read().split('\n')
    except:
        return []
    result = []
    for f in log_file:
        if(len(f.strip())>0):
            result.append(cal_osc_log(f))
    return result

if __name__ == '__main__':
    if len(parms) ==1:
        print("please input your requestID when process run!")
    else:
        acc_log  = get_acc_log(R6_OSC_LOG_DIR)
        osc_log = get_osc_log(R6_OSC_LOG_DIR)
        if acc_log:
            print("################ access log for requestID %s ##############"%(parms[1]))
            show_list(acc_log)
            print()
        if osc_log:
            print("################ osc log for requestID %s ##############"%(parms[1]))
            show_list(osc_log)
