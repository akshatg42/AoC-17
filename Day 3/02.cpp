#include<iostream>
using namespace std;

#define SIZE 100
#define INPUT 347991

int max_ = 1;

bool in_bounds(int x, int y){
    return x < SIZE && y < SIZE && x >=0 && y>=0;
}

void fill(int** array, int x, int y){
    int sum=0;
    if(in_bounds(x-1, y-1) && array[x-1][y-1] != -1) sum+=array[x-1][y-1];
    if(in_bounds(x-1, y) && array[x-1][y] != -1) sum+=array[x-1][y];
    if(in_bounds(x-1, y+1) && array[x-1][y+1] != -1) sum+=array[x-1][y+1];
    if(in_bounds(x, y-1) && array[x][y-1] != -1) sum+=array[x][y-1];
    if(in_bounds(x, y+1) && array[x][y+1] != -1) sum+=array[x][y+1];
    if(in_bounds(x+1, y-1) && array[x+1][y-1] != -1) sum+=array[x+1][y-1];
    if(in_bounds(x+1, y) && array[x+1][y] != -1) sum+=array[x+1][y];
    if(in_bounds(x+1, y+1) && array[x+1][y+1] != -1) sum+=array[x+1][y+1];
    array[x][y] = sum;
    if(sum > max_ && max_ < INPUT){
        max_ = sum;
    }
}

void fill_(int** array, int d){
    int start = d/2 - 1;
    int start_x = SIZE/2 + start, start_y = SIZE/2 + start + 1;
    //up
    for(int i=0; i<d-1; i++){
        fill(array, start_x-i, start_y);
    }
    //left
    for(int i=0; i<d; i++){
        fill(array, start_x-d+2, start_y-i);
    }
    //down
    for(int i=0; i<d; i++){
        fill(array, start_x-d+2+i, start_y-d+1);
    }
    // //right
    for(int i=0; i<d; i++){
        fill(array, start_x+1, start_y-d+1+i);
    }
}

int main(){
    int **array;
    array = new int*[SIZE];
    for(int i=0; i<SIZE; i++){
        array[i] = new int[SIZE];
    }
    for(int i=0; i<SIZE; i++){
        for(int j=0; j<SIZE; j++){
            array[i][j] = -1;
        }
    }
    int up=SIZE/2, down=SIZE/2, left=SIZE/2, right=SIZE/2;
    array[SIZE/2][SIZE/2] = 1;
    int k = 3;
    while(max_ < INPUT){
        fill_(array, k);
        k+=2;
    }
    cout<<max_<<endl;
}