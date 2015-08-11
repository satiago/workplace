//获取查询的参数
var train_date = document.getElementById("train_date").value.substring(0, 10);
var from_station = document.getElementById("fromStation").value;
var to_station = document.getElementById("toStation").value;

if(document.getElementById("sf1").checked === true)
{
  purpose_codes = "ADULT";
}
else
{
  purpose_codes = "0X00";
}

var log_url = "https://kyfw.12306.cn/otn/leftTicket/log?" +
            "leftTicketDTO.train_date=" + encodeURIComponent(train_date) + "&" +
            "leftTicketDTO.from_station=" + encodeURIComponent(from_station) + "&" +
            "leftTicketDTO.to_station=" + encodeURIComponent(to_station) + "&" +
            "purpose_codes=" + encodeURIComponent(purpose_codes);

var query_url = "https://kyfw.12306.cn/otn/leftTicket/queryT?" +
            "leftTicketDTO.train_date=" + encodeURIComponent(train_date) + "&" +
            "leftTicketDTO.from_station=" + encodeURIComponent(from_station) + "&" +
            "leftTicketDTO.to_station=" + encodeURIComponent(to_station) + "&" +
            "purpose_codes=" + encodeURIComponent(purpose_codes);           

//发送请求，接受数据
// 异步请求时
// xhr.onreadystatechange = function()
// {
//   if (xmlhttp.readyState==4 && xmlhttp.status==200)
//   {
    
//   }
// };

//车票信息处理
var query_tickets = function(tickets_data)
{
  //console.log(JSON.stringify(tickets_data));
  //数据处理,拿到所有车次二等座的票数，出发时间。
  var tickets_array = [];
  for(var i = 0; i < tickets_data.length; i++)
  {
    if(tickets_data[i].queryLeftNewDTO.ze_num != "--" && tickets_data[i].queryLeftNewDTO.ze_num != "无" && tickets_data[i].queryLeftNewDTO.ze_num != "*")
    {
      var tickets_info = {}; //js的对象，json格式
      tickets_info.station_train_code = tickets_data[i].queryLeftNewDTO.station_train_code;
      tickets_info.start_time = tickets_data[i].queryLeftNewDTO.start_time;
      tickets_info.ze_num = tickets_data[i].queryLeftNewDTO.ze_num;
      
      tickets_array.push(tickets_info);
    }
  }
  
  var tickets_str = "有票的车次为:" + "\n";
  for(i = 0; i < tickets_array.length; i++)
  {
     tickets_str += "车次:" + tickets_array[i].station_train_code + "=====" +
                    "发车时间:" + tickets_array[i].start_time + "=====" +
                    "二等座票数:" + tickets_array[i].ze_num + "\n";
  }
  alert(tickets_str);
  //console.log(JSON.stringify(tickets_array));
};

var xhr = new XMLHttpRequest();
xhr.open("GET", log_url, false);//同步请求
xhr.send();

//解析返回的json数据
var log_data = JSON.parse(xhr.responseText);

if(log_data.httpstatus == 200 && log_data.status === true)
{
  xhr.open("GET", query_url, false);//同步请求
  xhr.send();
  
  var query_data = JSON.parse(xhr.responseText);
  if(query_data.httpstatus == 200 && query_data.status === true)
  {
    query_tickets(query_data.data);
  }
  else
  {
    window.alert("query failed!");
  }
}
else
{
  window.alert("log failed!");
}