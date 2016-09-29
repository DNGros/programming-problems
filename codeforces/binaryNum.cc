#include <iostream>
#include <string>
using namespace std;

int main(){
    string num;
    getline(cin, num);
    int tail = num.length() - 1;
    int count = 0;
    while(tail > 0){
        if(num[tail] == '0'){
            tail -= 1;
        }
        else{
            int flipI = tail;
            while(flipI >= 0 && num[flipI] == '1'){
                num[flipI] = '0';
                flipI -= 1;
            }
            if(flipI >= 0){
                num[flipI] = '1';
            }
            else{
                tail += 1;
                num[tail] = '0';
                num[0] = '1';
            }
        }
        count += 1;
    }
    cout << count << endl;
}
