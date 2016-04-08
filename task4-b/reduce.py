#!/usr/bin/python
import sys
import os

agents = {}


current_agent_name = None

for line in sys.stdin:
    
    agent_name, revenue = line.strip().split("\t", 1)
    
    try:
        revenue = float(revenue)
    except ValueError:
        continue
    if agent_name == current_agent_name:
        agents[agent_name] += revenue
    else:
        agents[agent_name] = revenue
        current_agent_name = agent_name
            
    

names = sorted(agents, key=agents.__getitem__, reverse = True)

for a in names[:20]:
    print ("%s\t%0.2f" % (a, agents[a]))
