package main

import (
    "fmt"
    "strconv"
    "os"
    "math"
    "math/cmplx"
    "image"
    "image/png"
    "image/color"
)


// inMandelSet returns the number of iteration it takes to test for divergence // at any given point (x,y) on the complex plane.  If we can show that If we reach max_iterations without proving divergence 
// then we assume the point converges.

func inMandelSet(x, y float64, max_iteration int) int {
    var (
        k int           = 0
        z complex128    = 0
        c complex128    = complex(x, y)
    )
    for k =0; k < max_iteration; k++ {
        z = cmplx.Pow(z, 2) + c
        if cmplx.Abs(z) > 2 {
            return k
        }
    }
    return k
}

// drawDot adds a colored pixel to the input image.
// Does stuff to make nice colors for R,G,B

func drawDot(img *image.RGBA, q, r int, valueX, valueY float64, m int) {
    
    var myRed, myGreen, myBlue uint8
    i := inMandelSet(valueX, valueY, m)

    if  (i > (m/2)) && (i < (3*m/2)) {myGreen = uint8( i * 255 / m)}
    if (i > (m/3)) && (i < (m/2))  {myRed = uint8( i * 255 / m)}
    myBlue = uint8( i  * 255 / m )

    img.Set(q, r, color.RGBA{myRed, myGreen, myBlue , 255})
    return
}




// Main Thing

func main() {

    // some variables
    
    const (
        width          int = 4000  
        height         int = 4000
        max_iteration  int = 1000

        xo float64  =  0.001643721971153
        yo float64  = -0.822467633298876 
        Re float64  =  0.00000000001
    )


    w := float64(width)
    q := float64(height)
    deltaX := math.Abs(2 * Re ) / w
    deltaY := math.Abs( 2 * Re ) / q

    img := image.NewRGBA(image.Rect(0, 0, width, height))


    // Draw a red dot at each point inside the set.
    for q := 0; q < width; q++ {
        for r := 0; r < height; r++ {

            valueX := float64(q) * deltaX + xo - Re
            valueY := float64(r) * deltaY + yo - Re

            drawDot(img, q, r, valueX, valueY, max_iteration)
        }
        fmt.Println(width-q-1)
    }
    




    // Save to a special filename
    // The filename is going to have the input values built into it.
    // This should help separate the files after making them.

    xoStr := strconv.FormatFloat(xo, 'E', -1, 64)
    yoStr := strconv.FormatFloat(yo, 'E', -1, 64)
    ReStr := strconv.FormatFloat(Re, 'E', -1, 64)
    itStr := strconv.Itoa(max_iteration)

    filename := "Mandelbrot Set "+"x=("+xoStr+") y=("+yoStr+") r=("+ReStr+") iterations=("+itStr+").png"
    fmt.Println("Image has been created! \n Filename: "+filename)

    filepath := "coolPictures/"+filename

    // This part actually creates the file itself.

    f, _ := os.OpenFile(filepath, os.O_WRONLY|os.O_CREATE, 0600)
    defer f.Close()
    png.Encode(f, img)
}


// Adding Parralellism for multicore processors




