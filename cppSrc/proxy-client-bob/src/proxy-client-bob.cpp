//客户端 Bob

#include "proxy-client-bob.h"

static int own_id = 0;

void* recv_thread(void* arg)
{
	char recvbuff[1024] = {0};
	int recvfd = *((int*)arg);
	DATA_HEAD data_head;
	
	//接收数据
	while(1)
	{
		memset(recvbuff, 0, 1024);
		if( recv(recvfd, recvbuff, 1024, 0) == -1 )
		{
			printf("recv data failed!\n");
			pthread_exit((void*)0);
		}
		
		//解析数据包中的ID，保存
		//若sid = 0，为服务器端的消息，用来发送客户端ID，ID更新
		//若sid != 0，为转发消息，不需改变客户端ID，只转发
		memcpy(&data_head, recvbuff, sizeof(data_head));

		if(data_head.sid == 0)
		{
			own_id = data_head.rid;
		}

		printf("recv data: %s, from client ID: %d", recvbuff + sizeof(data_head), data_head.sid);
	}
	
	return (void *)1;
}

int main(int argc, char **argv)
{
	int sockfd;
	int recv_id;
	struct sockaddr_in servaddr;
	char buffer[1024] = {0};
	char data[1024] = {0};
	DATA_HEAD data_head;
	pthread_t rtid;
	
	if(argc != 3)
	{
		printf("usage:proxy-client-bob server-ip server-port\n");
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
	
	//等待服务器端回传ID
	sleep(2);

	//发送数据
	while(1)
	{
		//输入发送的数据
		printf("please input data to send:\n");
		memset(data, 0, 1024);
		
//		scanf("%s", buffer);(空格为断句处)
//		gets(buffer);（不安全）
		fgets(data, 1024, stdin);

		//输入发送的客户端ID
		printf("please input client ID to send:\n");
		scanf("%d", &recv_id);

		//构造发送数据包
		data_head.sid = own_id;
		data_head.rid = recv_id;
		data_head.length = strlen(data);

		memset(buffer, 0, 1024);
		memcpy(buffer, &data_head, sizeof(data_head));
		memcpy(buffer + sizeof(data_head), data, strlen(data));

		if( send(sockfd, buffer, 1024, 0) == -1 )
		{
			printf("send data failed!\n");
			return 0;
		}
	}

	return 1;
}
