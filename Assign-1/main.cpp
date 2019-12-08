#include <bits/stdc++.h>
using namespace std;

long long int coefficients[11];

long long int find_solution(long long int n, long long int x)
{
    long long int ans=0;
    for (int i=n;i>=0;i--)
    {
        ans += pow(x,i)*coefficients[i];
    }
    return ans;
}

int main()
{
    long long int n;

    cout<<"What is the power of the polynomial?"<<endl;
    cin>>n;
    for (int i=n;i>=0;i--)
    {
        cout<<"What is the coefficient of x to the power "<<i<<endl;
        cin>>coefficients[i];
    }

    srand(time(0));

    long long int pos_number;
    long long int neg_number;

    while(true)
    {
        pos_number = rand()%10;
         long long int solution_number = find_solution(n, pos_number);
        if (solution_number == 0)
        {
            cout<<"The solution is "<<pos_number<<endl;
        }
        if (solution_number > 0)
        {
            break;
        }
    }

    while(true)
    {
        neg_number = rand()%10;
        long long int solution_number = find_solution(n, neg_number);
        if (solution_number == 0)
        {
            cout<<"The solution is "<<neg_number<<endl;
            return 0;
        }
        if (solution_number < 0)
        {
            break;
        }
        neg_number = -neg_number;
        solution_number = find_solution(n, neg_number);
        if (solution_number == 0)
        {
            cout<<"The solution is "<<neg_number<<endl;
            return 0;
        }
        if (solution_number < 0)
        {
            break;
        }
    }

    while (true)
    {
        cout<<"Pos "<<pos_number<<" neg "<<neg_number<<endl;
        long long int solution_number = (pos_number + neg_number)/2;
        cout<<"Number "<<solution_number<<endl;

        long long int solution = find_solution(n, solution_number);
        cout<<"Solution "<<solution<<endl;

        if (solution < 0)
        {
            neg_number = solution_number;
        }
        else if (solution > 0)
        {
            pos_number = solution_number;
        }
        else 
        {
            cout<<"The solution is obv "<<solution_number<<endl;
            break;
        }
    }
    
}
