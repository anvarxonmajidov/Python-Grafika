import math 

print( "%s" % 10    )
print("%s - %s - %s" % (10, 20, 30) )
print( "%(name)s - %(year)s" % {"year": 1947, "name": "Erkin"} )
print( "'%d' - '%05d'" % (3, 3) )
print(  "'%10d' - '%-10d'" % (3, 3) )
print("'%3s''%10s'" % ("string", "string") )
print("%s %f %.2f" % (math.pi, math.pi, math.pi) )
print( "%s" % ("Обычная строка"))
print("%s %s %s" % (10, 10.52, [1, 2, 3]))
print( "%r" % ("Обычная строка") )
print( "%d %d %d" % (10, 25.6, -80)  )
print("'{0:10}' '{1:3}'".format(3, "string") )
print("'{0:{1}}'".format(3, 10))
print( "'{0:<10}' '{1:>10}' '{2:^10}'".format(3, 3, 3) )
print("'{0:=10}' '{1:=10}'".format(-3, 3) )
print("'{0:=010}' '{1:=010}'".format(-3, 3))
print("'{0:+}' '{1:+}' '{0:-}' '{1:-}'".format(3, -3))
print("'{0:b}' '{0:#b}'".format(3) )
print("'{0:c}'".format(100) )
print("'{0:d}' '{0:o}' '{0:#o}'".format(511)  )
print("'{0:x}' '{0:#x}'".format(255)  )
print("'{0:X}' '{0:#X}'".format(255) )
print("'{0:f}' '{1:f}' '{2:f}'".format(30, 18.6578145, -2.5) )
print("'{0:.7f}' '{1:.2f}'".format(18.6578145, -2.5)  )
print("'{0:e}' '{1:e}'".format(3000, 18657.81452) )
print("'{0:E}' '{1:E}'".format(3000, 18657.81452)  )
print("'{0:%}' '{1:.4%}'".format(0.086578, 0.000086578) )