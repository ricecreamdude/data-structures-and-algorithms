// https://www.geeksforgeeks.org/unique-paths-in-a-grid-with-obstacles/


let uniquePaths = (m,n) => {

  let aux = createGrid(m,n);

  for(let i = 1; i < m; i++){
    for (let j = 1; j < n; j++){
      aux[i][j] = aux[i-1][j] + aux[i][j-1];
    }
  }



  return aux[m-1][n-1];

}

let createGrid = (x,y) => {

  let grid = [];

  for (let i = 0; i < x; i++){
    grid.push([]);
    for (let j = 0; j < y; j++){
      grid[i].push(1);
    }
  }


  return grid;
}


console.log('SHOULD EQUAL 20:' ,uniquePaths(4,4)); 