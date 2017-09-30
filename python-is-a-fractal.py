"""
Fractal Generation in Python
by Chris Achenbach

Using the Escape Time Algorithm to generate the Mandelbrot Set.

The program is composed of several parts:
- given variables (input)
- initalizing data
- main algorithm
- image output
"""




# -----------------------------------------------------------------------------
# Given Variables
# -----------------------------------------------------------------------------


# First, we want to determine the desired pixel size of the output image.

image_width_max = 100
image_height_max = 50


# We also want to set a Maximum Iteration value.
# This influences how many iterations we use to look for a limit.

max_iteration = 200


# Based on the equation for the Mandelbrot set, we want to determine scale.
# Mandelbrot's Equation:  z = x +  i * y
# We need to choose the x and y ranges we wish to investigate.

a = 0.001
b = 0.822
q = 0.1


x0, xf = -2.1, 1
y0, yf = -1, 1

x0, xf = a, a+q
x0, xf = a, a+q







# -----------------------------------------------------------------------------
# Initializing Data
# -----------------------------------------------------------------------------


# Given the x and y scalings and the desired image dimensions,
# assign x and y values to each Pixel, based on those scalings.
#     This can be achieved by finding the distances  |xf-x0| and |yf-y0|, 
# and dividing that by the number of pixels for each dimension.  

delta_x = abs(xf - x0) / image_width_max
delta_y = abs(yf - y0) / image_height_max


# We are going to initialize a matrix to represent a pixel mapping.
# NOTE: Notice that Matrix[0][5] = the point at (5,0).

pixel_Matrix = [ [0]*image_width_max  for _ in range(image_height_max) ]






# -----------------------------------------------------------------------------
# Algorithm
# -----------------------------------------------------------------------------



# First, we create a Function to check if a given x,y value is in the set.
# We define the recursion sequence as    z_{n+1} = z_{n} + (x + iy)
# Then, we check z_{n} for all n <= Max_Iterations, starting with z_{0} = 0.
# If we find ever find  |z_{n}| >= 2, then we assume the sequence diverges.
# After we reach the end of our iterations, we assume it converges.

def inMandelSet(x: int, y: int, max_iteration: int) -> int:
    """inMandelSet determines if complex(x,y) is in the mandelbrot set."""
    z = 0
    for k in range(max_iteration):
        z = z ** 2 + complex(x,y)
        if abs(z) > 2: return k
    return k




# For each pixel on our image, we check to see if it lies in the set.
# We use the previously defined function to assign values to our Pixel Matrix.

for Py in range(image_height_max):
    for Px in range(image_width_max):

        x = Px * delta_x + x0
        y = Py * delta_y + y0

        pixel_Matrix[Py][Px] = inMandelSet(x, y, max_iteration)




# TODO:
# The output of this algorithm is a value for each pixel based on the number of
# iterations it took to discover divergence.  
            

        

# -----------------------------------------------------------------------------
# Output as a String
# -----------------------------------------------------------------------------


# First, Initiate a String for making the text file, 

newString = ''

# Next, we want to add symbols or spaces to the string, as if they were pixels.
# a symbol '#' denotes that the point (x,y) is in the set.
# an empty space ' ' is for the points that are NOT in the set.
# Print a new line at the end of each row.
# Remember that this matrix is defined as Matrix[y][x].

for y in range(image_height_max):

    for x in range(image_width_max):

        myValue = pixel_Matrix[y][x] // (max_iteration // 10)

        if myValue == 10:   newString += '#'
        if myValue == 0:    newString += ' '
        else:               newString += str(myValue)

    newString += '\n'


# -----------------------------------------------------------------------------
# Creating Colors for Values
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Create a Text File with Mandelbrot Set
# -----------------------------------------------------------------------------


# Now, let's open a new file and write down our newly created string.

newFileName = 'python-mandelbrot-set'

with open( newFileName + '.txt', "w") as newFile:
    newFile.write(newString)



# -----------------------------------------------------------------------------
# Image Creation
# -----------------------------------------------------------------------------


# Now, let's open a new file and write down our newly created string.

newFileName = 'python-mandelbrot-set'

with open( newFileName + '.txt', "w") as newFile:
    newFile.write(newString)