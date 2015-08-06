//服务器端 Server
//当有客户端进行连接时，为客户端分配唯一的ID
//ID从1开始，服务器的ID为0
//服务器分配好ID后，通知客户端

#include "proxy-server.h"

//记录当前分配ID的数量
static int id_count = 0;
//记录当前分配的ID-SOCK对
static ID_SOCK id_sock[100] = 0;

//子线程，处理服务器端的数据接收
void* thread_transfer(void* arg)
{

	return ((void*) 1);
}

//子线程，处理服务器端的数据接收
void* thread_worker(void* arg)
{
	char buffer[1024];
	char data[1024];
	int workerfd;
	int transferfd;
	DATA_HEAD data_head;
	
	workerfd = *((int *)arg);
	//处理数据交互
	
	//清空缓存
	memset(buffer, 0, 1024);
	memset(data, 0, 1024);
		
	//分配ID
	data_head.sid = 0;
	data_head.rid = id_count + 1;
	
	//记录ID-SOCK对
	id_sock[data_head.rid].id = data_head.rid;
	id_sock[data_head.rid].sock = workerfd;

	//发送欢迎信息,信息中包含给当前客户端分配的ID
	snprintf(data, 1024, WELCOME, data_head.rid);
	data_head.length = strlen(data);

	//构造数据包
	memcpy(buffer, &data_head, sizeof(data_head));
	memcpy(buffer + sizeof(data_head), data, strlen(data));

	if( send(workerfd, buffer, strlen(buffer), 0) == -1 )
	{
		printf("send welcome failed!\n");
		close(workerfd);
		pthread_exit((void*)0);
	}
	
	while(1)
	{
		memset(&buffer, 0, 1024);
		if(recv(workerfd, buffer, 1024, 0) == -1)
		{
			printf("recv data failed!\n");
			close(workerfd);
			pthread_exit((void*)0);
		}
		
		//解析包头，判断数据包的转发地址并进行转发
		//转发时启动线程处理(暂无)
		memcpy(&data_head, buffer, sizeof(data_head));
		transferfd = id_sock[data_head.rid].sock;

		if( send(transferfd, buffer, strlen(buffer), 0) == -1 )
		{
			printf("transfer data failed!\n");
			close(transferfd);
			pthread_exit((void*)0);
		}

		printf("transfer data:%s, transfer ID:%d\n", buffer + sizeof(data_head), data_head.rid);
	}
	
	return ((void*) 1);
}

int main(int argc, char **argv)
{
	int sockfd, connfd;
	pthread_t tid;
	struct sockaddr_in servaddr;
	struct sockaddr accept_addr;
	socklen_t accept_addr_len;
	
	if(argc != 2)
	{
		printf("usage:proxy-server port\n");
		return 0;
	}
	
	//TODO:参数错误处理
	
	if( (sockfd = socket(AF_INET, SOCK_STREAM, 0)) < 0)
	{
		printf("create socket failed!\n");
		return 0;
	}
	
	memset(&servaddr, 0, sizeof(servaddr));
	servaddr.sin_family = AF_INET;
	servaddr.sin_addr.s_addr = htonl(INADDR_ANY);
	servaddr.sin_port = htons(atoi(argv[1]));
	
	//绑定
	if( bind(sockfd, (struct sockaddr*)&servaddr, sizeof(servaddr)) == -1 )
	{
		printf("bind failed!\n");
		return 0;
	}
	
	while(1)
	{
		//监听
		if(listen(sockfd, SOMAXCONN) == -1)
		{
			printf("listen failed!\n");
			return 0;
		}
	
		printf("-----wait for client----\n");
	
		//连接
		if( (connfd = accept(sockfd, &accept_addr, &accept_addr_len)) == -1 )
		{
			printf("accept failed!\n");
			return 0;
		}
		
		//启动线程，处理各自客户端的数据交互请求
		if( pthread_create(&tid, NULL, thread_worker, (void*)&connfd) != 0 )
		{
			printf("create thread failed!\n");
			return 0;
		}
		
	}
	
	return 1;
}

