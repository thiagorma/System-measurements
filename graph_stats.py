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
	status, intcp = commands.getstatusoutput("nstat -z -t 5 | grep TcpExtTCPHPHits")	
	status, drop = commands.getstatusoutput("nstat -z -t 5 | grep TcpExtTCPRcvCollapsed")
	drop_var = drop[32:38]	
	intcp_var = intcp[32:38]
	drop_varfloat = float(drop_var)
	intcp_varfloat = float(intcp_var)
        if intcp_varfloat == 0:
		intcp_varfloat = 1 
       	z=(drop_varfloat*100)/intcp_varfloat
	return "%2.2f" %z		

def main():
    print 'NO.  CPU MEMORY  DROP'
    plt.subplot(211)
    i=0
    while True:
        i+=1
        plt.ylim(0,105)
#        plt.xlim(0,60)
        cc=cpu()
        mm=mem()
        dd=drp()
        print i,'\t',cc,'\t',mm,'\t',dd
        c.append(cc)
        m.append(mm)
        d.append(dd)
        plt.grid(True)
        plt.xlabel('TIME')
        plt.ylabel('USAGE IN %')

        plt.title(' - - SYSTEM MONITOR - - ')
        dp='DROP ('+dd+'%)'
        ms='RAM  ('+mm+'%)'
        cs='CPU  ('+cc+'%)'
        plt.plot(d[-60:-1],'g', label=dp)
        plt.plot(m[-60:-1],'r', label=ms)
        plt.plot(c[-60:-1],'b', label=cs)
        plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.06,0,0.04), ncol=3)
        if len(c)>60:
            del c[0]
            del m[0]
            del d[0]
        plt.draw()
        matplotlib.interactive(True)
        plt.show()
	plt.show()
        plt.clf()
main()

