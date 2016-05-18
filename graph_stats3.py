#!/usr/bin/env python

import matplotlib.pyplot as plt
import matplotlib
import psutil
import commands

c=[]
m=[]
d=[]

def cpu():
	a=psutil.cpu_percent(interval = 0.1, percpu=False)
	return "%2.2f" %a

def mem():
	a=psutil.virtual_memory().percent
	return "%2.2f" %a

def drp():
	status, drop = commands.getstatusoutput("nstat -z --interval=60 | grep TcpExtTCPRcvCollapsed")
#	status, drop = commands.getstatusoutput("nstat -z --interval=60 | grep TcpExtListenDrops")
	drop_var = drop[32:38]	
	z = float(drop_var)
	return "%2.2f" %z		

def main():
    fig = plt.figure()
#    ax1 = fig.add_subplot(211)
#    ax2 = fig.add_subplot(212)
    print 'NO.  CPU  MEMORY  DROP'
    i=0	
    while True:
        ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)
        i+=1
        ax1.set_ylim(-5,105)
#	ax2.set_ylim(0,105)
#       ax1.set_xlim(0,60)
#	ax2.set_xlim(0,60)
        cc=cpu()
        mm=mem()
        dd=drp()

        print i,'\t',cc,'\t',mm,'\t',dd
        c.append(cc)
        m.append(mm)
        d.append(dd)

        ax1.grid(True)
#       ax1.set_xlabel('TIME')
        ax1.set_ylabel('USAGE IN %')

	ax2.grid(True)
	ax2.set_xlabel('TIME')
	ax2.set_ylabel('TOTAL')

        ax1.set_title('SYSTEM MONITOR')
        ax2.set_title('PACKET DROPPING INDICATOR')
	
	dp='DROP ('+dd+'%)'
        ms='RAM  ('+mm+'%)'
        cs='CPU  ('+cc+'%)'
        ax2.plot(d[-60:-1],'g', label=dp)
        ax1.plot(m[-60:-1],'r', label=ms)
        ax1.plot(c[-60:-1],'b', label=cs)
#       ax1.legend(loc='upper center', bbox_to_anchor=(0.5, -0.06,0,0.04), ncol=3)

        if len(c)>60:
            del c[0]
            del m[0]
	    
	if len(d)>60:
            del d[0]
	    
        plt.draw()
        matplotlib.interactive(True)
        plt.show()
	fig.clf()	
main()

