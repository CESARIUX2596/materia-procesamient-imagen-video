"use strict";

var canvas;
var gl;

var points = [];

var numTimesToSubdivide = 0;

var bufferId;
var slider;

function init()
{
    canvas = document.getElementById( "gl-canvas" );

    gl = WebGLUtils.setupWebGL( canvas );
    if ( !gl ) { alert( "WebGL isn't available" ); }

    //
    //  Configure WebGL
    //
    gl.viewport( 0, 0, canvas.width, canvas.height );
    gl.clearColor( 1.0, 1.0, 1.0, 1.0 );

    //  Load shaders and initialize attribute buffers

    var program = initShaders( gl, "vertex-shader", "fragment-shader" );
    gl.useProgram( program );

    // Load the data into the GPU

    bufferId = gl.createBuffer();
    gl.bindBuffer( gl.ARRAY_BUFFER, bufferId );
    gl.bufferData( gl.ARRAY_BUFFER, 8*Math.pow(3, 6), gl.STATIC_DRAW );



    // Associate out shader variables with our data buffer

    var vPosition = gl.getAttribLocation( program, "vPosition" );
    gl.vertexAttribPointer( vPosition, 2, gl.FLOAT, false, 0, 0 );
    gl.enableVertexAttribArray( vPosition );

    //// ---------------------------
    //// Agregar el slider en el programa
    //// y enlazarlo con la variable que indica el numero 
    //// de veces en que se haran subdivisiones del triangulo
    //// ---------------------------
    slider = document.getElementById("slider");
  
    slider.onchange = function(){
      numTimesToSubdivide = event.srcElement.value;
      render();
    };

    render();
}

function triangle( a, b, c )
{
    points.push( a, b, c );
}


//// ---------------------------
//// Generar la funcion Dividir triangulo
//// En vez de utilizar el operador suma
//// utiliza la funcion mix
//// ---------------------------

void divide_triangle(point2 a, point2 b, point2 c, int k)
{

    if (k > 0)
    {
        point2 ab = mix(a, b, 0.5);
        point2 ac = mix(a, c, 0.5);
        point2 bc = mix(b, c, 0.5);
        

        divide_triangle(a, ab, ac, k - 1);
        divide_triangle(c, ac, bc, k - 1);
        divide_triangle(b, bc, ab, k - 1);
    }
    else triangle(a,b,c);
}



function render()
{
    var vertices = [
        vec2( -1, -1 ),
        vec2(  0,  1 ),
        vec2(  1, -1 )
    ];
    points = [];

    //// ---------------------------
    //// Llamada del programa de la funcion para dividir triangulo
    //// especificando los tres vertices
    //// y la variable que indica el numero de veces para subdivision
    //// ---------------------------
    
    divide_triangle(vertices[0], vertices[1], vertices[2], numTimesToSubdivide);
  
    gl.bufferSubData(gl.ARRAY_BUFFER, 0, flatten(points));
    gl.clear( gl.COLOR_BUFFER_BIT );
    gl.drawArrays( gl.TRIANGLES, 0, points.length );
    points = [];
    //requestAnimFrame(render);
}

window.onload = init;