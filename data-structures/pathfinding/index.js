//Given size of grid m * n
//In any instance, you can go (x, y+1) or (x+1, y);


//Sample Grid:        
// Input: [[0, 0, 0],
//         [0, 1, 0],
//         [0, 0, 0]]

//0 means open space
//1 means occupied space

//Sample Output: 2  (there are two unique paths)
// function navigateGrid(){

// }


//Accessing values will be as follows:
//this.grid[x][y] => gridCell
class Grid {
  constructor(){
    this.grid = [];
  }

// This method should take in an array of arrays and build a grid out of the
// data provided. 
// Input: [[0, 0, 0],
//         [0, 1, 0],
//         [0, 0, 0]]
  buildGrid(array){

    let cell = new GridCell(array[0][0]);
  



  }

}

//Grid cells need to have a value, do they need coordinates?
class GridCell {
  constructor(value=null){
    this.value = value;
    // this.x = x;
    // this.y = y;
  }
}




function execute(){

  let testGrid = new Grid;
  let testGridValues = [
    [0]
  ]


  testGrid.buildGrid()


  console.log('running tests', testGrid);
}



execute();