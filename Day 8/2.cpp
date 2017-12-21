#include <vector>
#include <string>
#include <iostream>
#include <map>
using namespace std;

vector<string> split(string data){
    vector<string> output;
    int pos = data.find(" ");
    while (pos != string::npos){
        output.push_back(data.substr(0, pos));
        data = data.substr(pos + 1);
        pos = data.find(" ");
    }
    if(data.size() > 0){
        output.push_back(data);
    }
    return output;
}

int check_present(map<string, int> &regs, string register1){
    map<string, int>::iterator it;
    it = regs.find(register1);
    if(it == regs.end()){
        regs[register1] = 0;
    }
    return regs[register1];
}

void set_bool(bool &b, string s, int r2, int cons){
    if(s.compare(">") == 0){
        b = r2 > cons;
    }
    if(s.compare("<") == 0){
        b = r2 < cons;
    }
    if(s.compare(">=") == 0){
        b = r2 >= cons;
    }
    if(s.compare("<=") == 0){
        b = r2 <= cons;
    }
    if(s.compare("==") == 0){
        b = r2 == cons;
    }
    if(s.compare("!=") == 0){
        b = r2 != cons;
    }
}

int main(){
    string line;
    map <string, int> regs;
    int max = 0;
    while(getline(cin, line)){
        vector<string> equation = split(line);
        string reg1 = equation[0];
        string reg2 = equation[4];
        int r1 = check_present(regs, reg1);
        int r2 = check_present(regs, reg2);
        int cons=0;
        bool b = false;
        set_bool(b, equation[5], r2, stoi(equation[6]));
        if(b){
            cons = stoi(equation[2]);
            if(equation[1].compare("inc") == 0){
                regs[reg1]+=cons;
                if(regs[reg1] > max){
                    max = regs[reg1];
                }
            }
            else{
                regs[reg1]-=cons;
                if(regs[reg1] > max){
                    max = regs[reg1];
                }
            }
        }
    }
    cout<<max<<endl;
    return 0;
}