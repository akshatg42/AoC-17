#include <iostream>
#include <vector>

#define SIZE 16

using namespace std;

vector< vector<int> > heap;

bool check(vector<int> &array){
    for(size_t t=0; t<heap.size(); t++){
        int f = true;
        for(int i=0; i<SIZE; i++){
            if(array[i] == heap[t][i]) f = f&&true;
            else f = f&&false;
        }
        if(f) return true;
    }
    return false;
}

void redistribute(vector<int> &array){
    int max=-1, max_index=-1;
    for(int i=0; i<SIZE; i++){
        if(max < array[i]){
            max = array[i];
            max_index=i;
        }
    }
    int payload = array[max_index];
    array[max_index] = 0;
    int ite = max_index+1;
    while(payload > 0){
        array[ite%SIZE]++;
        ite++;
        payload--;
    }
}

int main(){
    vector<int> array;
    for(int i=0; i<SIZE; i++){
        int inp;
        cin>>inp;
        array.push_back(inp);
    }
    int ans=0;
    while(!check(array)){
        heap.push_back(array);
        redistribute(array);
        ans++;
    }
    cout<<ans<<endl;
}