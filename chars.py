#This is the data file for the pingpong ball clock

D       =  [[0,  0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26],
		    [0, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27],
		    [0, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
		    [0,107,106,105,104,103,102,101,100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81],
		    [0,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134],
		    [0,161,160,159,158,157,156,155,154,153,152,151,150,149,148,147,146,145,144,143,142,141,140,139,138,137,136,135],
		    [0,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188],
		    [0,215,214,213,212,211,210,209,208,207,206,205,204,203,202,201,200,199,198,197,196,195,194,193,192,191,190,189],
		    [0,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242],
		    [0,269,268,267,266,265,264,263,262,261,260,259,258,257,256,255,254,253,252,251,250,249,248,247,246,245,244,243],
		    [0,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290,291,292,293,294,295,296]]

def display():
	return(D)

def zero(origin_x, origin_y):
	return(D[origin_x][origin_y],D[origin_x][origin_y+1],D[origin_x][origin_y+2],D[origin_x][origin_y+3],D[origin_x+1][origin_y],D[origin_x+1][origin_y+3],D[origin_x+2][origin_y],D[origin_x+2][origin_y+3],D[origin_x+2][origin_y],D[origin_x+2][origin_y+3],D[origin_x+3][origin_y],D[origin_x+3][origin_y+3],D[origin_x+4][origin_y],D[origin_x+4][origin_y+3],D[origin_x+5][origin_y],D[origin_x+5][origin_y+3],D[origin_x+6][origin_y],D[origin_x+6][origin_y+1],D[origin_x+6][origin_y+2],D[origin_x+6][origin_y+3])

def one(origin_x, origin_y):
	return(D[origin_x][origin_y+3],D[origin_x+1][origin_y+3],D[origin_x+2][origin_y+3],D[origin_x+3][origin_y+3],D[origin_x+4][origin_y+3],D[origin_x+5][origin_y+3],D[origin_x+6][origin_y+3])

def two(origin_x, origin_y):
	return(D[origin_x][origin_y],D[origin_x][origin_y+1],D[origin_x][origin_y+2],D[origin_x][origin_y+3],D[origin_x+1][origin_y+3],D[origin_x+2][origin_y+3],D[origin_x+3][origin_y],D[origin_x+3][origin_y+1],D[origin_x+3][origin_y+2],D[origin_x+3][origin_y+3],D[origin_x+4][origin_y],D[origin_x+5][origin_y],D[origin_x+6][origin_y],D[origin_x+6][origin_y+1],D[origin_x+6][origin_y+2],D[origin_x+6][origin_y+3])

def three(origin_x, origin_y):
	return(D[origin_x][origin_y],D[origin_x][origin_y+1],D[origin_x][origin_y+2],D[origin_x][origin_y+3],D[origin_x+1][origin_y+3],D[origin_x+2][origin_y+3],D[origin_x+3][origin_y],D[origin_x+3][origin_y+1],D[origin_x+3][origin_y+2],D[origin_x+3][origin_y+3],D[origin_x+4][origin_y+3],D[origin_x+5][origin_y+3],D[origin_x+6][origin_y],D[origin_x+6][origin_y+1],D[origin_x+6][origin_y+2],D[origin_x+6][origin_y+3])

def four(origin_x, origin_y):
	return(D[origin_x][origin_y],D[origin_x][origin_y+3],D[origin_x+1][origin_y],D[origin_x+1][origin_y+3],D[origin_x+2][origin_y],D[origin_x+2][origin_y+3],D[origin_x+3][origin_y],D[origin_x+3][origin_y+1],D[origin_x+3][origin_y+2],D[origin_x+3][origin_y+3],D[origin_x+4][origin_y+3],D[origin_x+5][origin_y+3],D[origin_x+6][origin_y+3])

def five(origin_x, origin_y):
	return(D[origin_x][origin_y],D[origin_x][origin_y+1],D[origin_x][origin_y+2],D[origin_x][origin_y+3],D[origin_x+1][origin_y],D[origin_x+2][origin_y],D[origin_x+3][origin_y],D[origin_x+3][origin_y+1],D[origin_x+3][origin_y+2],D[origin_x+3][origin_y+3],D[origin_x+4][origin_y+3],D[origin_x+5][origin_y+3],D[origin_x+6][origin_y],D[origin_x+6][origin_y+1],D[origin_x+6][origin_y+2],D[origin_x+6][origin_y+3])

def six(origin_x, origin_y):
	return(D[origin_x][origin_y],D[origin_x][origin_y+1],D[origin_x][origin_y+2],D[origin_x][origin_y+3],D[origin_x+1][origin_y],D[origin_x+2][origin_y],D[origin_x+3][origin_y],D[origin_x+3][origin_y+1],D[origin_x+3][origin_y+2],D[origin_x+3][origin_y+3],D[origin_x+4][origin_y],D[origin_x+4][origin_y+3],D[origin_x+5][origin_y],D[origin_x+5][origin_y+3],D[origin_x+6][origin_y],D[origin_x+6][origin_y+1],D[origin_x+6][origin_y+2],D[origin_x+6][origin_y+3])

def seven(origin_x, origin_y):
	return(D[origin_x][origin_y],D[origin_x][origin_y+1],D[origin_x][origin_y+2],D[origin_x][origin_y+3],D[origin_x+1][origin_y+3],D[origin_x+2][origin_y+3],D[origin_x+3][origin_y+3],D[origin_x+4][origin_y+3],D[origin_x+5][origin_y+3],D[origin_x+6][origin_y+3])

def eight(origin_x, origin_y):
	return(D[origin_x][origin_y],D[origin_x][origin_y+1],D[origin_x][origin_y+2],D[origin_x][origin_y+3],D[origin_x+1][origin_y],D[origin_x+1][origin_y+3],D[origin_x+2][origin_y],D[origin_x+2][origin_y+3],D[origin_x+3][origin_y],D[origin_x+3][origin_y+1],D[origin_x+3][origin_y+2],D[origin_x+3][origin_y+3],D[origin_x+4][origin_y],D[origin_x+4][origin_y+3],D[origin_x+5][origin_y],D[origin_x+5][origin_y+3],D[origin_x+6][origin_y],D[origin_x+6][origin_y+1],D[origin_x+6][origin_y+2],D[origin_x+6][origin_y+3])

def nine(origin_x, origin_y):
	return(D[origin_x][origin_y],D[origin_x][origin_y+1],D[origin_x][origin_y+2],D[origin_x][origin_y+3],D[origin_x+1][origin_y],D[origin_x+1][origin_y+3],D[origin_x+2][origin_y],D[origin_x+2][origin_y+3],D[origin_x+3][origin_y],D[origin_x+3][origin_y+1],D[origin_x+3][origin_y+2],D[origin_x+3][origin_y+3],D[origin_x+4][origin_y+3],D[origin_x+5][origin_y+3],D[origin_x+6][origin_y],D[origin_x+6][origin_y+1],D[origin_x+6][origin_y+2],D[origin_x+6][origin_y+3])

def A(origin_x, origin_y):
	return(D[origin_x][origin_y],D[origin_x][origin_y+1],D[origin_x][origin_y+2],D[origin_x][origin_y+3],D[origin_x+1][origin_y],D[origin_x+1][origin_y+3],D[origin_x+2][origin_y],D[origin_x+2][origin_y+3],D[origin_x+3][origin_y],D[origin_x+3][origin_y+1],D[origin_x+3][origin_y+2],D[origin_x+3][origin_y+3],D[origin_x+4][origin_y],D[origin_x+4][origin_y+3],D[origin_x+5][origin_y],D[origin_x+5][origin_y+3],D[origin_x+6][origin_y],D[origin_x+6][origin_y+3])

	#we need to return the char and then the last x of the char