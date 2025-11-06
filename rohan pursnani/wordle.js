// paste the following code into the editor at this site: https://editor.p5js.org/

function setup() {
  createCanvas(700, 700);
}

function draw() {
  
  gridSpacing=5
  squareSize=75
  rowCount=6
  colCount=5
  gridWidth = colCount * squareSize + (colCount - 1) * gridSpacing
  gridHeight=rowCount*squareSize+(rowCount-1)*gridSpacing
  hGap=width-gridWidth
  vGap=height-gridHeight
  print(gridWidth)
  print(gridHeight)
  print(hGap)
  print(vGap)
  leftMargin=hGap/2;
  topMargin=vGap/2;
  bgcolor=color(178,236,93)
  background(bgcolor);
  
  for(let rowNum=0; rowNum<rowCount; rowNum++){
    //draw row
    for(let colNum=0; colNum<colCount; colNum++){
      //draw box
      square(leftMargin+colNum*(gridSpacing+squareSize),
             topMargin+rowNum*(gridSpacing+squareSize),
             squareSize)
    }
  }
  row1=["q","w","e","r","t","y","u","i","o","p"]
  row2=["a","s","d","f","g","h","j","k","l"]
  row3=["z","x","c","v","b","n","m"]
  
  for(let qNum=0; qNum<row1.length; qNum++){
    text(row1[qNum],qNum*30,60)
  }
  // for(let aNum=0; aNum<row2.length; aNum++)
  // for(let zNum=0; zNum<row3.length; zNum++)
 
  noLoop()
}
