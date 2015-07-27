#include <stdio.h>  
#include <stdlib.h>  
#include <string.h>  
#include <errno.h>  
#include <sys/types.h>  
#include <sys/socket.h>  
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>

#include <pthread.h>

#define WELCOME "welcome, you are log in, ID is %d!\n"

//结构体

//传输的数据包头结构
//由服务器端发起的传输，sid=0
//由服务器端中转的传输，sid=发送方ID
typedef struct _data_head
{
	int sid; //发送方ID
	int rid; //接收方ID
	int length; //发送的数据长度
}DATA_HEAD;

//保存对应的ID和sock
typedef struct _id_sock
{
	int id;
	int sock;
}ID_SOCK;




