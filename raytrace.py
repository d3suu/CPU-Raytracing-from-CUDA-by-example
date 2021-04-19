from PIL import Image
import math

IMG_X,IMG_Y = 4000, 4000

image = Image.new("RGB", (IMG_X,IMG_Y) )

# Sphere
r,g,b = 56,105,202 #light blue
#r,g,b = 255,255,255 #white
#radius = 700
radius = (IMG_X+IMG_Y)/8 #1/4 of image size
x,y,z = (IMG_X/2),(IMG_Y/2),75

# Spheres
spheres = []
spheres.append({'r':56,'g':105,'b':202,'radius':400,'x':1500,'y':2500,'z':10000})
spheres.append({'r':240,'g':19,'b':19,'radius':(IMG_X+IMG_Y)/8,'x':(IMG_X/2),'y':(IMG_Y/2),'z':50})
print(spheres)
n = 0

def hit(ox, oy, sx, sy, sz, sradius):
        global n
        dx = ox-sx
        dy = oy-sy
        if(dx*dx + dy*dy < sradius*sradius):
                dz = math.sqrt( sradius*sradius - dx*dx - dy*dy )
                n = dz / math.sqrt( sradius*sradius )
                return dz + sz
        return -2e10

# Raytrace
for xx in range(0,IMG_X):
        for yy in range(0,IMG_Y):
                a_r,a_g,a_b = 0,0,0
                pr,pg,pb = 0,0,0
                maxz = -2e10
                for s in spheres:
                        t = hit(xx,yy,s['x'],s['y'],s['z'],s['radius'])
                        if(t > maxz):
                                #print("HIT! " + str(xx) + ", " + str(yy))
                                fscale = n
                                pr = int(s['r'] * fscale)
                                pg = int(s['g'] * fscale)
                                pb = int(s['b'] * fscale)
                                maxz = t
                        image.putpixel( (xx,yy), (pr,pg,pb) )

image.save('raytrace.png')
