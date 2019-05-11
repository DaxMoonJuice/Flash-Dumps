import spidev

def initDevice(bus,device):
	spi=spidev.SpiDev()
	spi.open(bus,device)
	spi.max_speed_hz=5000
	spi.mode=0b01	
	spi.lsbfirst=False
	
	return spi

def readID(spi):
	
	print spi.xfer2(['90H',0,0,0,0,0])
	


bus=0
device=1

flash=initDevice(bus,device)
readID(flash)

