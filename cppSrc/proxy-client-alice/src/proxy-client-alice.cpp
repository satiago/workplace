//客户端 Alice

#include "proxy-client-alice.h"

void* recv_thread(void* arg)
{
	char recvbuff[1024] = {0};
	int recvfd = *((int*)arg);
	
	//接收数据
	while(1)
	{
		memset(recvbuff, 0, 1024);
		if( recv(recvfd, recvbuff, 1024, 0) == -1 )
		{
			printf("recv data failed!\n");
			pthread_exit((void*)0);
		}
		
		printf("recv data:%s", recvbuff);
	}
	
	return (void *)1;
}

int main(int argc, char **argv)
{
	int sockfd;
	struct sockaddr_in servaddr;
	char buffer[1024] = {0};
	pthread_t rtid;
	
	if(argc != 3)
	{
		printf("usage:proxy-client-alice server-ip server-port\n");
		return 0;
	}
	
	//TODO:输入参数的错误处理
	
	if( (sockfd = socket(AF_INET, SOCK_STREAM, 0)) < 0)
	{
		printf("create sock failed\n");
		return 0;
	}
	
	memset(&servaddr, 0, sizeof(servaddr));
	servaddr.sin_family = AF_INET;
	
	servaddr.sin_port = htons(atoi(argv[2]));
	servaddr.sin_addr.s_addr = inet_addr(argv[1]);
	
	//连接
	if( connect(sockfd, (struct sockaddr*)&servaddr, sizeof(servaddr)) < 0 )
	{
		printf("connect failed!\n");
		return 0;
	}
	
	//数据传输
	//启动线程接收数据
	if( pthread_create(&rtid, NULL, recv_thread, (void*)&sockfd) != 0 )
	{
		printf("create thread failed!\n");
		return 0;
	}
	
	//发送数据
	while(1)
	{
		printf("please input data to send:\n");
		memset(buffer, 0, 1024);
		
//		scanf("%s", buffer);
//		gets(buffer);
		fgets(buffer, 1024, stdin);
		if( send(sockfd, buffer, 1024, 0) == -1 )
		{
			printf("send data failed!\n");
			return 0;
		}
	}
	
	
	return 1;
}
