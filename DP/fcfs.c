#include<stdio.h>

struct process_node{
	
	int pno;
	int arr;
	int burst;
	int wait;
	int turn;
	int response;
	int completed;

};

int main()
{
	
	int n;
	printf("Enter number of processes");
	scanf("%d",&n);
	struct process_node p[5];
	for(int i=0;i<n;i++)
	{
		printf("Enter arrival and burst time for process : %d \n" ,i+1);
		scanf("%d %d",&p[i].arr,&p[i].burst);
		p[i].pno=i+1;
	}
	
	for(int i=0;i<n-1;i++)
	{
		for(int j=0;j<n-i-1;j++)
		{
			if(p[j].arr>p[j+1].arr)
			{
				struct process_node temp=p[j];
				p[j]=p[j+1];
				p[j+1]=temp;
			}
		}
	}
	
	int time=0;
	for(int i=0;i<n;i++)
	{
		p[i].completed=time+p[i].burst;
		time+=p[i].burst;
		p[i].turn=p[i].completed-p[i].arr;
		p[i].wait=p[i].turn-p[i].burst;
		p[i].response=p[i].wait;
	}
	
	for(int i=0;i<n;i++)
	{
		
		printf("%d   %d   %d   %d   %d   %d",p[i].arr,p[i].burst,p[i].completed,p[i].turn,p[i].wait,p[i].response);
		printf("\n");
	}
	
	for(int i=0;i<n;i++)
	{
		printf("P(%d): (%d - %d)\n",p[i].pno,p[i].completed-p[i].burst,p[i].completed);
	}


}
