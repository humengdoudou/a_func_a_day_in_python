import numpy as np

# step 1
x = np.array([3, 1, 2])
print "np.argsort(x): "
print np.argsort(x)

y = np.array([[0, 3], [2, 2]])
print "y: "
print y

print "np.argsort(y, axis=0): "
print np.argsort(y, axis=0)   # by axis 0, column

print "np.argsort(y, axis=1): "
print np.argsort(y, axis=1)   # by axis 1, row

# Sorting with keys:

z = np.array([(1, 0), (0, 1)], dtype=[('x', '<i4'), ('y', '<i4')])
print z

print "np.argsort(z, order=('x','y')): "
print np.argsort(z, order=('x','y'))

print ("np.argsort(z, order=('y','x')): "
print np.argsort(z, order=('y','x'))



# step 2
print np.argsort(x)       # ascend
print np.argsort(-x)      # descend
print x[np.argsort(x)]    # get a sorted ascend 1d array by argsort 
print x[np.argsort(-x)]   # get a sorted descend 1d array by argsort

m = x[np.argsort(x)]
print m
print m[::-1]
