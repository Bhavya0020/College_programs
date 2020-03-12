#include<stdio.h>

struct stud
{
    int sub1;
    int sub2;
    int sub3;
    float avg;
    char grade;    
}s[1000];


void input(int n)
{
    //          Input...
    for(int i=0;i<n;i++)
    {
        scanf("%d%d%d",s[i].sub1,s[i].sub2,s[i].sub3);
    }
}

void display(int n)
{
    //          Display...
    for(int i=0;i<n;i++)
    {
        printf("%d%d%d%f%c",s[i].sub1,s[i].sub2,s[i].sub3,s[i].avg,s[i].grade);
    }
}

void grade_and_avg(int n)
{
    // float avg;
    for(int i=0;i<n;i++)
    {
        s[i].avg=(s[i].sub1+s[i].sub2+s[i].sub3)/3;
    }

    for(int i=0;i<n;i++)
    {
        if(s[i].avg>=90.00)
            s[i].grade='A';
        else if(s[i].avg<90 && s[i].avg>=80 )
            s[i].grade='B';
        else if(s[i].avg<80 && s[i].avg>=70 )
            s[i].grade='C';
        else if(s[i].avg<70 && s[i].avg>=60 )
            s[i].grade='B';
        else
        {
            s[i].grade='F';
        }
        
    }
}


int main()
{
    int n;
    printf("Enter the number of students");
    scanf("%d",n);
    input(n);
    grade_and_avg(n);
    display(n);

    
    
}