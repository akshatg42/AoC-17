#include<iostream>
using namespace std;

#define SIZE 101

bool isValid(int x){
    if(x>=0 && x<SIZE){
        return true;
    }
    return false;
}

void fill(int x, int y, int**array){
    if(isValid(x+1)){
        if(isValid(y)){
            if(array[x+1][y]!=-1){
                array[x][y]+=array[x+1][y];
            }
        }
        if(isValid(y+1)){
            if(array[x+1][y+1]!=-1){
                array[x][y]+=array[x+1][y+1];
            }
        }
        if(isValid(y-1)){
            if(array[x+1][y-1]!=-1){
                array[x][y]+=array[x+1][y-1];
            }
        }
    }
    // if(isValid(y+1)){
    //     if(isValid(y)){
    //         if(array[x+1][y]!=-1){
    //             array[x][y]+=array[x+1][y];
    //         }
    //     }
    //     if(isValid(y+1)){
    //         if(array[x+1][y+1]!=-1){
    //             array[x][y]+=array[x+1][y+1];
    //         }
    //     }
    //     if(isValid(y-1)){
    //         if(array[x+1][y-1]!=-1){
    //             array[x][y]+=array[x+1][y-1];
    //         }
    //     }
    // }
}

int main(){
    int array[101][101];
    for(int i=0; i<101; i++){
        for(int j=0; j<101; j++){
            array[i][j]=-1;
        }
    }
    int curr = 1;
    int row = 51;
    int leftB=51, rightB=51, upB=51, downB=51;
    while(true){
        if(currX>leftB && currX<rightB){
            array[currX][currY]=0;
            fill(currX, currY, array);
            currX++;
        }
    }
    for(int i=1; i<101; i++){

    }
}