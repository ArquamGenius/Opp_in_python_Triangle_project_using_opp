import math



class Triangle:
    def __init__(self,base,height):
        self.base=base;
        self.height=height;
#"""
#classs about:
#    **
#    * *
#    *  *    hypotenus
#opp.*   *
#    *    *
#    *     *
#    ********
#       
#    adjacent
#"""

class Righttriangle(Triangle):
	
	
	
	
	
	def __init__(self,hypotenuse,opposite,adjacent):
		self.adjacent=adjacent;
		self.hypotenuse=hypotenuse;
		self.opposite=opposite;
		
		
		if(self.hypotenuse=="?"):
			Ans=math.sqrt((opposite**2)+(self.adjacent**2));
			self.hypotenuse=Ans;
			
			
		elif(self.opposite=="?"):
			Ans=math.sqrt((self.hypotenuse**2)-(self.adjacent**2));
			self.opposite=Ans;
			
			

		
		elif(self.adjacent=="?"):  
			Ans=math.sqrt((self.hypotenuse**2)-(self.opposite**2));
			self.adjacent=Ans;



#Hypo()==hypotenuse;       
#                           
#         *
#         * *
#         *  *
#         *   *
#opposite *    *  hypotenuse==??
#         *     *
#         *      *
#         *********       
#         adjacent
#
#hypo**2=opp**2  + adja**2
#
#This function may calculate Hypotenuse:
#"""

	
#------------------------------------------------------------------------
#"""
#Function name:"Oppo();"


#Oppo==opposite;       
#                           
#         *
#         * *
#         *  *
#         *   *
#oppo==?? *    *  hypotenuse
#         *     *
#         *      *
#         *********       
#         adjacent

#oppo**2==hypo**2  - adja**2

#This function may calculate Oppsite:
#"""


#"""
#Function name:"Adja();"
#Adja==adjacent;       
#                           
#         *
#         * *
#         *  *
#         *   *
#oppo==?? *    *  hypotenuse
#         *     *
#         *      *
#         *********       
#         adjacent
#
#adja**2==hypo**2  - oppo**2
#
#This function may calculate Adjacent:
#
#"""

						
			
 

	def Hypo(self):
		Ans=math.sqrt((self.opposite**2)+(self.adjacent**2));
		return Ans;

          
	def Oppo(self):
		Ans=math.sqrt((self.hypotenuse**2)-(self.adjacent**2));
		return Ans;                              



	def Adja(self):
		Ans=math.sqrt((self.hypotenuse**2)-(self.opposite**2));
		return Ans;
		
										
		
	def Area(self):
		Ans=(1/2)*(self.adjacent)*(self.opposite);
		return Ans;
	
	
	
	def Sin(self):
		Ans_sine=(self.opposite)/(self.hypotenuse);
		return Ans_sine;
#+-----------------------------+
#Arcsine() is invers function
#it returns angle bases on side ratio in triangle
#+-----------------------------+			
	def Arcsin(self):
		Ratio=(self.opposite)/(self.hypotenuse);
		Angle_radian=math.asin(Ratio);
		Digree=((180)/(math.pi))*Angle_radian;
		return Digree;
		
		
	def Cos(self):
		pass;
	
	def Arccos(self):
		pass;
		
	
	def Tan(self):
		pass;
		
	def Arctan(self):
		pass;
		
		


   	                                                                                                                                                                                                                                                      


#-----------------------------------------------------------------        
#++++++++++
#ifing for calculate if tow were given
#++++++++++ 


                                      
if(__name__=="__main__"):
	hhh=Righttriangle(2,1,"?");
	print(hhh.Hypo())
	print(hhh.Oppo())
	print(hhh.Adja())
	print(hhh.Area())
	print(hhh.Sin())
	print(hhh.Arcsin())



