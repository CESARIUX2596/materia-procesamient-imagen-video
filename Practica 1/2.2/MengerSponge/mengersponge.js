"use strict";

var canvas;
var gl;

var points = [];
var colors = [];
var numTimesToSubdivide = 0;
// var numVertices  = 36;

var axis = 0;
var xAxis = 0;
var yAxis =1;
var zAxis = 2;

//// ---------------------------
//// Declarar theta como un vector 
//// de tres elementos
//// ---------------------------

var theta = [0,0,0];

var thetaLoc;

    var vertices = [
        vec3( -0.5, -0.5,  0.5 ),
        vec3( -0.5,  0.5,  0.5 ),
        vec3(  0.5,  0.5,  0.5 ),
        vec3(  0.5, -0.5,  0.5 ),
        vec3( -0.5, -0.5, -0.5 ),
        vec3( -0.5,  0.5, -0.5 ),
        vec3(  0.5,  0.5, -0.5 ),
        vec3(  0.5, -0.5, -0.5 )
    ];

    var vertexColors = [
        // vec4( 0.0, 0.0, 0.0, 1.0 ),  // black
        vec4( 1.0, 0.0, 0.0, 1.0 ),  // red
        vec4( 1.0, 1.0, 0.0, 1.0 ),  // yellow
        vec4( 0.0, 1.0, 0.0, 1.0 ),  // green
        vec4( 0.0, 0.0, 1.0, 1.0 ),  // blue
        vec4( 1.0, 0.0, 1.0, 1.0 ),  // magenta
        // vec4( 1.0, 1.0, 1.0, 1.0 ),  // white
        vec4( 0.0, 1.0, 1.0, 1.0 )   // cyan
    ];

// indices of the 12 triangles that compise the cube

var indices = [
    1, 0, 3,
    3, 2, 1,
    2, 3, 7,
    7, 6, 2,
    3, 0, 4,
    4, 7, 3,
    6, 5, 1,
    1, 2, 6,
    4, 5, 6,
    6, 7, 4,
    5, 4, 0,
    0, 1, 5
];

function init()
{   
    // window.cancelAnimationFrame(requestId);
    points = [];
    colors = [];
    numTimesToSubdivide =  document.getElementById("slider").value -1;
    dividirCubo(vertices[0],vertices[1],vertices[2],vertices[3],vertices[4],vertices[5],vertices[6],vertices[7],numTimesToSubdivide);
    canvas = document.getElementById( "gl-canvas" );

    gl = WebGLUtils.setupWebGL( canvas );
    if ( !gl ) { alert( "WebGL isn't available" ); }

    gl.viewport( 0, 0, canvas.width, canvas.height );
    gl.clearColor( 1.0, 1.0, 1.0, 1.0 );

    gl.enable(gl.DEPTH_TEST);;

    //
    //  Load shaders and initialize attribute buffers
    //
    var program = initShaders( gl, "vertex-shader", "fragment-shader" );
    gl.useProgram( program );

    // array element buffer

    // var iBuffer = gl.createBuffer();
    // gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, iBuffer);
    // gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, new Uint8Array(indices), gl.STATIC_DRAW);

    // color array atrribute buffer

    var cBuffer = gl.createBuffer();
    gl.bindBuffer( gl.ARRAY_BUFFER, cBuffer );
    gl.bufferData( gl.ARRAY_BUFFER, flatten(colors), gl.STATIC_DRAW );

    var vColor = gl.getAttribLocation( program, "vColor" );
    gl.vertexAttribPointer( vColor, 4, gl.FLOAT, false, 0, 0 );
    gl.enableVertexAttribArray( vColor );

    // vertex array attribute buffer

    var vBuffer = gl.createBuffer();
    gl.bindBuffer( gl.ARRAY_BUFFER, vBuffer );
    gl.bufferData( gl.ARRAY_BUFFER, flatten(points), gl.STATIC_DRAW );

    var vPosition = gl.getAttribLocation( program, "vPosition" );
    gl.vertexAttribPointer( vPosition, 3, gl.FLOAT, false, 0, 0 );
    gl.enableVertexAttribArray( vPosition );

    thetaLoc = gl.getUniformLocation(program, "theta");


//// ---------------------------
//// Agregar interaccion para la funciÃ³n de rotaciÃ³n. 
//// Declarar un evento para cada boton
//// ---------------------------

    document.getElementById( "xButton" ).onclick = function () {
        axis = xAxis;
    };
    document.getElementById( "yButton" ).onclick = function () {
        axis = yAxis;
    };
    document.getElementById( "zButton" ).onclick = function () {
        axis = zAxis;
    };

    render();
}

function dividirCubo( a,b,c,d,e,f,g,h, count )
{
    // check for end of recursion
    if ( count === 0 ) {
        cubo(a,b,c,d,e,f,g,h);
    }
    else {
        var a1 = mix( a, b, 1/3  );
        var a3 = mix( a, d, 1/3  );
        var a2 = vec3(a3[0],a1[1],a[2]);
        var a4 = mix( a, e, 1/3  );
        var a5 = vec3(a1[0],a1[1],a4[2]);
        var a6 = vec3(a2[0],a1[1],a4[2]);
        var a7 = vec3(a3[0],a3[1],a6[2]);

        var b0 = mix( b,a, 1/3  );
        var b2 = mix( b,c, 1/3  );
        var b3 = vec3( b2[0],b0[1],b2[2] );
        var b5 = mix( b,f, 1/3  );
        var b4 = vec3( b0[0], b0[1], b5[2] );
        var b6 = vec3( b2[0],b2[1],b5[2] );
        var b7 = vec3(b6[0],b3[1],b6[2]);

        var c1 = mix( c,b, 1/3  );
        var c3 = mix( c,d, 1/3  );
        var c0 = vec3(c1[0],c3[1],c1[2]);
        var c6 = mix( c,g, 1/3  );
        var c5 = vec3(c1[0],c6[1],c6[2]);
        var c4 = vec3(c5[0],c3[1],c5[2]);
        var c7 = vec3(c3[0],c3[1],c6[2]);

        var d0 = mix( d,a, 1/3  );
        var d2 = mix( d,c, 1/3  );
        var d1 = vec3( d0[0],d2[1],d2[2] );
        var d7 = mix( d,h, 1/3  );
        var d4 = vec3( d0[0], d0[1], d7[2] );
        var d6 = vec3( d2[0],d2[1],d7[2] );
        var d5 = vec3(d1[0],d1[1],d6[2]);

        var e0 = mix( e,a, 1/3  );
        var e5 = mix( e,f, 1/3  );
        var e7 = mix( e,h, 1/3  );
        var e1 = vec3(e5[0],e5[1],e0[2]);
        var e2 = vec3(e7[0],e1[1],e1[2]);
        var e3 = vec3(e7[0],e7[1],e0[2]);
        var e6 = vec3(e2[0],e2[1],e5[2]);

        var f1 = mix( f,b, 1/3  );
        var f4 = mix( f,e, 1/3  );
        var f6 = mix( f,g, 1/3  );
        var f0 = vec3( f4[0],f4[1],f1[2] );
        var f2 = vec3( f6[0], f6[1], f1[2] );
        var f7 = vec3(f6[0],f4[1],f6[2]);
        var f3 = vec3( f7[0],f7[1],f0[2] );
        
        var g2 = mix( g,c, 1/3  );
        var g5 = mix( g,f, 1/3  );
        var g7 = mix( g,h, 1/3  );
        var g1 = vec3(g5[0],g5[1],g2[2]);
        var g3 = vec3(g7[0],g7[1],g2[2]);
        var g0 = vec3(g1[0],g7[1],g1[2]);
        var g4 = vec3(g0[0],g0[1],g7[2]);

        var h3 = mix( h,d, 1/3  );
        var h4 = mix( h,e, 1/3  );
        var h6 = mix( h,g, 1/3  );
        var h0 = vec3( h4[0],h4[1],h3[2] );
        var h1 = vec3(h0[0],h6[1],h0[2]);
        var h2 = vec3( h6[0], h6[1], h1[2] );
        var h5 = vec3( h1[0],h1[1],h6[2] );

        --count;
        dividirCubo( a, a1,a2,a3,a4,a5,a6,a7, count );
        dividirCubo( a1, b0,b3,a2,a5,b4,b7,a6, count );
        dividirCubo( b0, b,b2,b3,b4,b5,b6,b7, count );
        dividirCubo( b3, b2,c1,c0,b7,b6,c5,c4, count );
        dividirCubo( c0, c1,c,c3,c4,c5,c6,c7, count );
        dividirCubo( d1, c0,c3,d2,d5,c4,c7,d6, count );
        dividirCubo( d0, d1,d2,d,d4,d5,d6,d7, count );
        dividirCubo( a3, a2,d1,d0,a7,a6,d5,d4, count );

        dividirCubo( a4, a5,a6,a7,e0,e1,e2,e3, count );
        dividirCubo( b4, b5,b6,b7,f0,f1,f2,f3, count );
        dividirCubo( c4, c5,c6,c7,g0,g1,g2,g3, count );
        dividirCubo( d4, d5,d6,d7,h0,h1,h2,h3, count );

        dividirCubo( e0, e1,e2,e3,e,e5,e6,e7, count );
        dividirCubo( e1, f0,f3,e2,e5,f4,f7,e6, count );
        dividirCubo( f0, f1,f2,f3,f4,f,f6,f7, count );
        dividirCubo( f3, f2,g1,g0,f7,f6,g5,g4, count );
        dividirCubo( g0, g1,g2,g3,g4,g5,g,g7, count );
        dividirCubo( h1, g0,g3,h2,h5,g4,g7,h6, count );
        dividirCubo( h0, h1,h2,h3,h4,h5,h6,h, count );
        dividirCubo( e3, e2,h1,h0,e7,e6,h5,h4, count );        
    }
}
function cubo(a,b,c,d,e,f,g,h){
    cuadrado(a,b,c,d,0);
    cuadrado(h,g,f,e,1);
    cuadrado(e,f,b,a,2);
    cuadrado(d,c,g,h,3);
    cuadrado(b,f,g,c,4);
    cuadrado(e,a,d,h,5);
}
function cuadrado(a,b,c,d,color){
    var vColor = vertexColors[color];
    points.push(b,a,d,d,c,b);
    colors.push(vColor,vColor,vColor,vColor,vColor,vColor)
}
window.onload = init;
function render()
{
    gl.clear( gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);

    //// ---------------------------
    //// Calcular el incremento de cada angulo
    //// de rotacion en los elementos de theta
    //// ---------------------------
    theta[axis] += 1.0;  
  
  
    gl.uniform3fv(thetaLoc, theta);


    gl.drawArrays( gl.TRIANGLES ,0,points.length);
    // console.log(points.length);


    requestAnimFrame( render );
}