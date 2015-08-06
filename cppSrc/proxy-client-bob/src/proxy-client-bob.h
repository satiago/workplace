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

typedef struct _data_head
{
	int sid; //发送方ID
	int rid; //接收方ID
	int length; //发送的数据长度
}DATA_HEAD;
