

function msg() {
    var a = document.getElementById('output').textContent ;
    var lines = a.split("\n");
    var text_list = [];
    for (var line = 0; line < lines.length; line++) {
        text_list.push(lines[line]);
    }

    document.getElementById('output2').textContent = "";
    // console.log(typeof text_list);
    for( var x of text_list) {
        //console.log( x);
        if(x.includes("end")){
            x = x.replace("end","ENDED");
            document.getElementById('output2').textContent += x;
        }
        
    }
  }