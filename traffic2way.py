import Adafruit_BBIO.GPIO as GPIO
import time
import math

road1r="P8_15"
road1y="P8_14"
road1g="P8_13"
road2r="P8_16"
road2y="P8_17"
road2g="P8_18"
road3r="P8_10"
road3y="P8_11"
road3g="P8_12"
road4r="P8_7"
road4y="P8_8"
road4g="P8_9"
disp11="P9_26"#MSB
disp12="P9_24"
disp13="P9_23"
disp14="P9_22"#LSB
disp21="P9_42"#MSB
disp22="P9_41"
disp23="P9_30"
disp24="P9_27"#LSB
disp31="P9_13"#MSB
disp32="P9_12"
disp33="P9_11"
disp34="P8_19"#LSB
disp41="P9_21"#MSB
disp42="P9_16"
disp43="P9_15"
disp44="P9_14"#LSB

class traffic:

	GPIO.setup(road1r,GPIO.OUT)
	GPIO.setup(road1y,GPIO.OUT)
	GPIO.setup(road1g,GPIO.OUT)
        GPIO.setup(road2r,GPIO.OUT)
	GPIO.setup(road2y,GPIO.OUT)
        GPIO.setup(road2g,GPIO.OUT)
   	GPIO.setup(road3r,GPIO.OUT)
        GPIO.setup(road3y,GPIO.OUT)
        GPIO.setup(road3g,GPIO.OUT)
        GPIO.setup(road4r,GPIO.OUT)
        GPIO.setup(road4y,GPIO.OUT)
        GPIO.setup(road4g,GPIO.OUT)
	GPIO.setup(disp11,GPIO.OUT)
	GPIO.setup(disp12,GPIO.OUT)
	GPIO.setup(disp13,GPIO.OUT)
        GPIO.setup(disp14,GPIO.OUT)
	GPIO.setup(disp21,GPIO.OUT)
        GPIO.setup(disp22,GPIO.OUT)
        GPIO.setup(disp23,GPIO.OUT)
        GPIO.setup(disp24,GPIO.OUT)
	GPIO.setup(disp31,GPIO.OUT)
        GPIO.setup(disp32,GPIO.OUT)
        GPIO.setup(disp33,GPIO.OUT)
        GPIO.setup(disp34,GPIO.OUT)
        GPIO.setup(disp41,GPIO.OUT)
        GPIO.setup(disp42,GPIO.OUT)
        GPIO.setup(disp43,GPIO.OUT)
        GPIO.setup(disp44,GPIO.OUT)

	def init_state(self):
		GPIO.output(road1r,GPIO.HIGH)
		GPIO.output(road1y,GPIO.HIGH)
		GPIO.output(road1g,GPIO.HIGH)
		GPIO.output(road2r,GPIO.HIGH)
                GPIO.output(road2y,GPIO.HIGH)
                GPIO.output(road2g,GPIO.HIGH)
		GPIO.output(road3r,GPIO.HIGH)
                GPIO.output(road3y,GPIO.HIGH)
                GPIO.output(road3g,GPIO.HIGH)
                GPIO.output(road4r,GPIO.HIGH)
                GPIO.output(road4y,GPIO.HIGH)
                GPIO.output(road4g,GPIO.HIGH)
		GPIO.output(disp11,GPIO.HIGH)
	        GPIO.output(disp12,GPIO.HIGH)
       		GPIO.output(disp13,GPIO.HIGH)
       		GPIO.output(disp14,GPIO.HIGH)
                GPIO.output(disp21,GPIO.HIGH)
                GPIO.output(disp22,GPIO.HIGH)
                GPIO.output(disp23,GPIO.HIGH)
                GPIO.output(disp24,GPIO.HIGH)
                GPIO.output(disp31,GPIO.HIGH)
                GPIO.output(disp32,GPIO.HIGH)
                GPIO.output(disp33,GPIO.HIGH)
                GPIO.output(disp34,GPIO.HIGH)
                GPIO.output(disp41,GPIO.HIGH)
                GPIO.output(disp42,GPIO.HIGH)
                GPIO.output(disp43,GPIO.HIGH)
                GPIO.output(disp44,GPIO.HIGH)
		return;

        def disp1(self,t):
		if(t==1):
			GPIO.output(disp11,GPIO.LOW)
			GPIO.output(disp12,GPIO.LOW)
			GPIO.output(disp13,GPIO.LOW)
                        GPIO.output(disp14,GPIO.HIGH)

		elif(t==2):
                        GPIO.output(disp11,GPIO.LOW)
                        GPIO.output(disp12,GPIO.LOW)
                        GPIO.output(disp13,GPIO.HIGH)
                        GPIO.output(disp14,GPIO.LOW)

		elif(t==3):
                        GPIO.output(disp11,GPIO.LOW)
                        GPIO.output(disp12,GPIO.LOW)
                        GPIO.output(disp13,GPIO.HIGH)
                        GPIO.output(disp14,GPIO.HIGH)

		
                elif(t==4):
                        GPIO.output(disp11,GPIO.LOW)
                        GPIO.output(disp12,GPIO.HIGH)
                        GPIO.output(disp13,GPIO.LOW)
                        GPIO.output(disp14,GPIO.LOW)

                elif(t==5):
                        GPIO.output(disp11,GPIO.LOW)
                        GPIO.output(disp12,GPIO.HIGH)
                        GPIO.output(disp13,GPIO.LOW)
                        GPIO.output(disp14,GPIO.HIGH)

                elif(t==6):
                        GPIO.output(disp11,GPIO.LOW)
                        GPIO.output(disp12,GPIO.HIGH)
                        GPIO.output(disp13,GPIO.HIGH)
                        GPIO.output(disp14,GPIO.LOW)


                elif(t==7):
                        GPIO.output(disp11,GPIO.LOW)
                        GPIO.output(disp12,GPIO.HIGH)
                        GPIO.output(disp13,GPIO.HIGH)
                        GPIO.output(disp14,GPIO.HIGH)

	        elif(t==8):
                        GPIO.output(disp11,GPIO.HIGH)
                        GPIO.output(disp12,GPIO.LOW)
                        GPIO.output(disp13,GPIO.LOW)
                        GPIO.output(disp14,GPIO.LOW)

                elif(t==9):
                        GPIO.output(disp11,GPIO.HIGH)
                        GPIO.output(disp12,GPIO.LOW)
                        GPIO.output(disp13,GPIO.LOW)
                        GPIO.output(disp14,GPIO.HIGH)


                elif(t==0):
                        GPIO.output(disp11,GPIO.LOW)
                        GPIO.output(disp12,GPIO.LOW)
                        GPIO.output(disp13,GPIO.LOW)
                        GPIO.output(disp14,GPIO.LOW)

		elif(t==10):
                        GPIO.output(disp11,GPIO.HIGH)
                        GPIO.output(disp12,GPIO.HIGH)
                        GPIO.output(disp13,GPIO.HIGH)
                        GPIO.output(disp14,GPIO.HIGH)
                        return;

	def disp2(self,t):
                if(t==1):
                        GPIO.output(disp21,GPIO.LOW)
                        GPIO.output(disp22,GPIO.LOW)
                        GPIO.output(disp23,GPIO.LOW)
                        GPIO.output(disp24,GPIO.HIGH)

                elif(t==2):
                        GPIO.output(disp21,GPIO.LOW)
                        GPIO.output(disp22,GPIO.LOW)
                        GPIO.output(disp23,GPIO.HIGH)
                        GPIO.output(disp24,GPIO.LOW)

                elif(t==3):
                        GPIO.output(disp21,GPIO.LOW)
                        GPIO.output(disp22,GPIO.LOW)
                        GPIO.output(disp23,GPIO.HIGH)
                        GPIO.output(disp24,GPIO.HIGH)


                elif(t==4):
                        GPIO.output(disp21,GPIO.LOW)
                        GPIO.output(disp22,GPIO.HIGH)
                        GPIO.output(disp23,GPIO.LOW)
                        GPIO.output(disp24,GPIO.LOW)

                elif(t==5):
                        GPIO.output(disp21,GPIO.LOW)
                        GPIO.output(disp22,GPIO.HIGH)
                        GPIO.output(disp23,GPIO.LOW)
                        GPIO.output(disp24,GPIO.HIGH)

		elif(t==6):
                        GPIO.output(disp21,GPIO.LOW)
                        GPIO.output(disp22,GPIO.HIGH)
                        GPIO.output(disp23,GPIO.HIGH)
                        GPIO.output(disp24,GPIO.LOW)


                elif(t==7):
                        GPIO.output(disp21,GPIO.LOW)
                        GPIO.output(disp22,GPIO.HIGH)
                        GPIO.output(disp23,GPIO.HIGH)
                        GPIO.output(disp24,GPIO.HIGH)

                elif(t==8):
                        GPIO.output(disp21,GPIO.HIGH)
                        GPIO.output(disp22,GPIO.LOW)
                        GPIO.output(disp23,GPIO.LOW)
                        GPIO.output(disp24,GPIO.LOW)

		elif(t==9):
                        GPIO.output(disp21,GPIO.HIGH)
                        GPIO.output(disp22,GPIO.LOW)
                        GPIO.output(disp23,GPIO.LOW)
                        GPIO.output(disp24,GPIO.HIGH)


                elif(t==0):
                        GPIO.output(disp21,GPIO.LOW)
                        GPIO.output(disp22,GPIO.LOW)
                        GPIO.output(disp23,GPIO.LOW)
                        GPIO.output(disp24,GPIO.LOW)
                        return;

	def disp3(self,t):
                if(t==1):
                        GPIO.output(disp31,GPIO.LOW)
                        GPIO.output(disp32,GPIO.LOW)
                        GPIO.output(disp33,GPIO.LOW)
                        GPIO.output(disp34,GPIO.HIGH)

                elif(t==2):
                        GPIO.output(disp31,GPIO.LOW)
                        GPIO.output(disp32,GPIO.LOW)
                        GPIO.output(disp33,GPIO.HIGH)
                        GPIO.output(disp34,GPIO.LOW)

                elif(t==3):
                        GPIO.output(disp31,GPIO.LOW)
                        GPIO.output(disp32,GPIO.LOW)
                        GPIO.output(disp33,GPIO.HIGH)
                        GPIO.output(disp34,GPIO.HIGH)


                elif(t==4):
                        GPIO.output(disp31,GPIO.LOW)
                        GPIO.output(disp32,GPIO.HIGH)
                        GPIO.output(disp33,GPIO.LOW)
                        GPIO.output(disp34,GPIO.LOW)
 
		elif(t==5):
                        GPIO.output(disp31,GPIO.LOW)
                        GPIO.output(disp32,GPIO.HIGH)
                        GPIO.output(disp33,GPIO.LOW)
                        GPIO.output(disp34,GPIO.HIGH)

                elif(t==6):
                        GPIO.output(disp31,GPIO.LOW)
                        GPIO.output(disp32,GPIO.HIGH)
                        GPIO.output(disp33,GPIO.HIGH)
                        GPIO.output(disp34,GPIO.LOW)

		elif(t==7):
                        GPIO.output(disp31,GPIO.LOW)
                        GPIO.output(disp32,GPIO.HIGH)
                        GPIO.output(disp33,GPIO.HIGH)
                        GPIO.output(disp34,GPIO.HIGH)
		
                elif(t==8):
                        GPIO.output(disp31,GPIO.HIGH)
                        GPIO.output(disp32,GPIO.LOW)
                        GPIO.output(disp33,GPIO.LOW)
                        GPIO.output(disp34,GPIO.LOW)

                elif(t==9):
                        GPIO.output(disp31,GPIO.HIGH)
                        GPIO.output(disp32,GPIO.LOW)
                        GPIO.output(disp33,GPIO.LOW)
                        GPIO.output(disp34,GPIO.HIGH)

		elif(t==0):
                        GPIO.output(disp31,GPIO.LOW)
                        GPIO.output(disp32,GPIO.LOW)
                        GPIO.output(disp33,GPIO.LOW)
                        GPIO.output(disp34,GPIO.LOW)
                        return;


	def disp4(self,t):
                if(t==1):
                        GPIO.output(disp41,GPIO.LOW)
                        GPIO.output(disp42,GPIO.LOW)
                        GPIO.output(disp43,GPIO.LOW)
                        GPIO.output(disp44,GPIO.HIGH)

                elif(t==2):
                        GPIO.output(disp41,GPIO.LOW)
                        GPIO.output(disp42,GPIO.LOW)
                        GPIO.output(disp43,GPIO.HIGH)
                        GPIO.output(disp44,GPIO.LOW)

                elif(t==3):
                        GPIO.output(disp41,GPIO.LOW)
                        GPIO.output(disp42,GPIO.LOW)
                        GPIO.output(disp43,GPIO.HIGH)
                        GPIO.output(disp44,GPIO.HIGH)


                elif(t==4):
                        GPIO.output(disp41,GPIO.LOW)
                        GPIO.output(disp42,GPIO.HIGH)
                        GPIO.output(disp43,GPIO.LOW)
                        GPIO.output(disp44,GPIO.LOW)
                        
		elif(t==5):
                        GPIO.output(disp41,GPIO.LOW)
                        GPIO.output(disp42,GPIO.HIGH)
                        GPIO.output(disp43,GPIO.LOW)
                        GPIO.output(disp44,GPIO.HIGH)

                elif(t==6):
                        GPIO.output(disp41,GPIO.LOW)
                        GPIO.output(disp42,GPIO.HIGH)
                        GPIO.output(disp43,GPIO.HIGH)
                        GPIO.output(disp44,GPIO.LOW)


                elif(t==7):
                        GPIO.output(disp41,GPIO.LOW)
                        GPIO.output(disp42,GPIO.HIGH)
                        GPIO.output(disp43,GPIO.HIGH)
                        GPIO.output(disp44,GPIO.HIGH)

		elif(t==8):
                        GPIO.output(disp41,GPIO.HIGH)
                        GPIO.output(disp42,GPIO.LOW)
                        GPIO.output(disp43,GPIO.LOW)
                        GPIO.output(disp44,GPIO.LOW)

                elif(t==9):
                        GPIO.output(disp41,GPIO.HIGH)
                        GPIO.output(disp42,GPIO.LOW)
                        GPIO.output(disp43,GPIO.LOW)
                        GPIO.output(disp44,GPIO.HIGH)

		elif(t==0):
                        GPIO.output(disp41,GPIO.LOW)
                        GPIO.output(disp42,GPIO.LOW)
                        GPIO.output(disp43,GPIO.LOW)
                        GPIO.output(disp44,GPIO.LOW)
                        return;

	def disp_off(self):
		self.disp1(0);
		self.disp2(0);
		self.disp3(0);
                self.disp4(0);
                return;	

	def state(self,x):
		if(x==1):
			GPIO.output(road1r,GPIO.HIGH)
	                GPIO.output(road1y,GPIO.HIGH)
        	        GPIO.output(road1g,GPIO.LOW)
               		GPIO.output(road2r,GPIO.LOW)
             	        GPIO.output(road2y,GPIO.HIGH)
               		GPIO.output(road2g,GPIO.HIGH)
               		GPIO.output(road3r,GPIO.HIGH)
                        GPIO.output(road3y,GPIO.HIGH)
                        GPIO.output(road3g,GPIO.LOW)
                        GPIO.output(road4r,GPIO.LOW)
                        GPIO.output(road4y,GPIO.HIGH)
                        GPIO.output(road4g,GPIO.HIGH)
   			
			for t in range(9,0,-1):
				self.disp1(t)
  				self.disp3(t)
				time.sleep(1)
			self.disp_off()
    			

		elif(x==2):
                        GPIO.output(road1r,GPIO.HIGH)
                        GPIO.output(road1y,GPIO.LOW)
                        GPIO.output(road1g,GPIO.HIGH)
                        GPIO.output(road2r,GPIO.LOW)
                        GPIO.output(road2y,GPIO.HIGH)
                        GPIO.output(road2g,GPIO.HIGH)
                        GPIO.output(road3r,GPIO.HIGH)
                        GPIO.output(road3y,GPIO.LOW)
                        GPIO.output(road3g,GPIO.HIGH)
                        GPIO.output(road4r,GPIO.LOW)
                        GPIO.output(road4y,GPIO.HIGH)
                        GPIO.output(road4g,GPIO.HIGH)

                        for t in range(5,0,-1):
                                self.disp1(t)
				self.disp3(t)
                                time.sleep(1)
                        self.disp_off()


		                
	        elif(x==3):
                        GPIO.output(road1r,GPIO.LOW)
                        GPIO.output(road1y,GPIO.HIGH)
                        GPIO.output(road1g,GPIO.HIGH)
                        GPIO.output(road2r,GPIO.HIGH)
                        GPIO.output(road2y,GPIO.HIGH)
                        GPIO.output(road2g,GPIO.LOW)
                        GPIO.output(road3r,GPIO.LOW)
                        GPIO.output(road3y,GPIO.HIGH)
                        GPIO.output(road3g,GPIO.HIGH)
                        GPIO.output(road4r,GPIO.HIGH)
                        GPIO.output(road4y,GPIO.HIGH)
                        GPIO.output(road4g,GPIO.LOW)

                        for t in range(9,0,-1):
                                self.disp2(t)
				self.disp4(t)
                                time.sleep(1)
                        self.disp_off()

		elif(x==4):
                        GPIO.output(road1r,GPIO.LOW)
                        GPIO.output(road1y,GPIO.HIGH)
                        GPIO.output(road1g,GPIO.HIGH)
                        GPIO.output(road2r,GPIO.HIGH)
                        GPIO.output(road2y,GPIO.LOW)
                        GPIO.output(road2g,GPIO.HIGH)
                        GPIO.output(road3r,GPIO.LOW)
                        GPIO.output(road3y,GPIO.HIGH)
                        GPIO.output(road3g,GPIO.HIGH)
                        GPIO.output(road4r,GPIO.HIGH)
                        GPIO.output(road4y,GPIO.HIGH)
                        GPIO.output(road4g,GPIO.LOW)

                        for t in range(5,0,-1):
                                self.disp2(t)
				self.disp4(t)
                                time.sleep(1)
                        self.disp_off()
				
         	elif(x==5):
                        GPIO.output(road1r,GPIO.HIGH)
                        GPIO.output(road1y,GPIO.HIGH)
                        GPIO.output(road1g,GPIO.LOW)
                        GPIO.output(road2r,GPIO.LOW)
                        GPIO.output(road2y,GPIO.HIGH)
                        GPIO.output(road2g,GPIO.HIGH)
                        GPIO.output(road3r,GPIO.HIGH)
                        GPIO.output(road3y,GPIO.HIGH)
                        GPIO.output(road3g,GPIO.LOW)
                        GPIO.output(road4r,GPIO.LOW)
                        GPIO.output(road4y,GPIO.HIGH)
                        GPIO.output(road4g,GPIO.HIGH)

                        for t in range(9,0,-1):
                                self.disp3(t)
                                self.disp1(t)
                                time.sleep(1)
                        self.disp_off()

		elif(x==6):
                        GPIO.output(road1r,GPIO.HIGH)
                        GPIO.output(road1y,GPIO.LOW)
                        GPIO.output(road1g,GPIO.HIGH)
                        GPIO.output(road2r,GPIO.LOW)
                        GPIO.output(road2y,GPIO.HIGH)
                        GPIO.output(road2g,GPIO.HIGH)
                        GPIO.output(road3r,GPIO.HIGH)
                        GPIO.output(road3y,GPIO.LOW)
                        GPIO.output(road3g,GPIO.HIGH)
                        GPIO.output(road4r,GPIO.LOW)
                        GPIO.output(road4y,GPIO.HIGH)
                        GPIO.output(road4g,GPIO.HIGH)

                        for t in range(5,0,-1):
                                self.disp3(t)
				self.disp1(t)
                                time.sleep(1)
                        self.disp_off()

 		elif(x==7):
                        GPIO.output(road1r,GPIO.HIGH)
                        GPIO.output(road1y,GPIO.HIGH)
                        GPIO.output(road1g,GPIO.LOW)
                        GPIO.output(road2r,GPIO.LOW)
                        GPIO.output(road2y,GPIO.HIGH)
                        GPIO.output(road2g,GPIO.HIGH)
                        GPIO.output(road3r,GPIO.LOW)
                        GPIO.output(road3y,GPIO.HIGH)
                        GPIO.output(road3g,GPIO.HIGH)
                        GPIO.output(road4r,GPIO.HIGH)
                        GPIO.output(road4y,GPIO.HIGH)
                        GPIO.output(road4g,GPIO.LOW)

                        for t in range(9,0,-1):
                                self.disp4(t)
				self.disp1(t)
                                time.sleep(1)
                        self.disp_off()

 		elif(x==8):
                        GPIO.output(road1r,GPIO.HIGH)
                        GPIO.output(road1y,GPIO.LOW)
                        GPIO.output(road1g,GPIO.HIGH)
                        GPIO.output(road2r,GPIO.LOW)
                        GPIO.output(road2y,GPIO.HIGH)
                        GPIO.output(road2g,GPIO.HIGH)
                        GPIO.output(road3r,GPIO.LOW)
                        GPIO.output(road3y,GPIO.HIGH)
                        GPIO.output(road3g,GPIO.HIGH)
                        GPIO.output(road4r,GPIO.HIGH)
                        GPIO.output(road4y,GPIO.LOW)
                        GPIO.output(road4g,GPIO.HIGH)

                        for t in range(5,0,-1):
                                self.disp4(t)
				self.disp1(t)
                                time.sleep(1)
                        self.disp_off()
                        return;

obj = traffic()
obj.init_state()
while True:
	for i in range(1,9):
		obj.state(i);
		time.sleep(1);	


