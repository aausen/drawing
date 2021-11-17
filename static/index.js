'use strict';

function draw(){
    const canvas = document.getElementById("paint");
    if (canvas.getContext) {
        const ctx = canvas.getContext("2d");
        
        const myCanvas = document.getElementById("myCanvas");
        let myCanvas_style = getComputedStyle(myCanvas);
        canvas.width = 500;
        canvas.height = 250;

        let mouse = {x:0, y:0};

    // refactor into another function for mouse recapture //
        canvas.addEventListener('mousemove', function(e){
            mouse.x = e.pageX - this.offsetLeft;
            mouse.y = e.pageY - this.offsetTop;
        }, false);
    
    // refactor for new fuction for drawing
        ctx.lineJoin = 'round';
        ctx.lineCap = 'round';

        ctx.strokeStyle = 'red';

        function getColor(color){
            strokeStyle = color;
        }

        function getSize(size){
            ctx.lineWidth = size;
        }

        canvas.addEventListener('mousedown', function(e) {
            ctx.beginPath();
            ctx.moveTo(mouse.x, mouse.y);

            canvas.addEventListener('mousemove', onPaint, false);
        }, false);

        canvas.addEventListener('mouseup', function() {
            canvas.removeEventListener('mousemove', onPaint, false);
        }, false);

        let onPaint = function() {
            ctx.lineTo(mouse.x, mouse.y);
            ctx.stroke();
        };

    } else {
        console.log("it's not working!")
        // replace with code for browsers that don't suport canvas 
    }
}

draw();



// ctx.moveTo(0, 0);

// ctx.lineTo(500, 250)

// ctx.stroke();