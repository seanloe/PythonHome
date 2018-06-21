#! python3
#
#google map basic application
#
#import googlemaps as gm
from mypack.network.maplib import *
from googlemaps.exceptions import TransportError
import sys



def main():
	input_args = sys.argv
	myclient = init_googlemap_client()
	try:
	    if input_args[1]=='location':
	    	if len(input_args)<3:
	    		print('please input address!')
	    	print(input_args[2])
	    	print(get_location(myclient, input_args[2]))
	    if input_args[1]=='distance':
	    	if len(input_args)<4:
	    		print('please input 2 addresses')
	    	distance,duration = get_distance_and_duraion(myclient,input_args[2],input_args[3])
	    	print('Distance:%.2f km Duration:%i mins'%(distance/1000,duration/60))

	except (TransportError) as e:
		print('network Error occurred')


if __name__=='__main__':main()