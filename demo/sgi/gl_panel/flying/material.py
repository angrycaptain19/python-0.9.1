import light

def mkmatdict():
	#
	return {
	    'material 1': light.m1,
	    'material 2': light.m2,
	    'material 3': light.m3,
	    'material 4': light.m4,
	    'material 5': light.m5,
	    'material 6': light.m6,
	    'material 7': light.m7,
	    'material 8': light.m8,
	    'material 9': light.m9,
	}

materdict = mkmatdict ()

def mklichtdict():
	#
	return {'light 1': light.light1, 'light 2': light.light2}

lichtdict = mklichtdict ()
