import os
from datetime import datetime, timedelta
def format_compute_time(time):
    if ":" in time:
        h, m = map(int, time.split(":"))
    else:
        h, m = int(time), 0
    return h, m

def hrs_12(times):
    hrs = []
    for start, end in times:
        hrs.append(int(start.split(":")[0]) if ":" in start else int(start))
        hrs.append(int(end.split(":")[0]) if ":" in end else int(end))
    return all(hr >= 13 for hr in hrs)

def hours24(h, fmt, prvt):
    if not fmt:
        return h
    if h < prvt:
        return h + 12
    return h                                                                
                                                                        
def calculatetime(start, end, fmt, prvt):
    starthr, startmin = format_compute_time(start)
    endhr, endmin = format_compute_time(end)   
    starthr = hours24(starthr, fmt, prvt)
    endhr = hours24(endhr, fmt, starthr)
    start = datetime(2025,2,1, starthr, startmin)
    end = datetime(2025,2,1, endhr, endmin)
    
    if end <= start:
        end += timedelta(hours=12)
    return (end - start).total_seconds()/3600
    
def sum_timesheet(path):
    total_time = 0
    
    with open(path, 'r') as f:
      for line in f:
          line = line.strip()
          if line:
              times = [tuple(time.strip().split("-")) for time in line.split(",")]
              prvt = 0
              fmt = hrs_12(times)
              
              for start, end in times:                                                
                  total_time += calculatetime(start.strip(), end.strip(), fmt, prvt)
                  prvt, _ = format_compute_time(end)
    return total_time
