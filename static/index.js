'use strict';

function draw(){
    var canvas = document.getElementById("myCanvas");
    if (canvas.getContext) {
        var ctx = canvas.getContext("2d");
        ctx.fillStyle = 'rbg(200, 0, 0)';
        ctx.fillRect(10, 10, 50, 50)

        ctx.fillStyle = 'rbga(0, 0, 200. 0.5)';
        ctx.fillRect(30, 30, 50, 50)
    } else {
        console.log("it's not working!")
    }
}

draw();



// ctx.moveTo(0, 0);

// ctx.lineTo(500, 250)

// ctx.stroke();