document.addEventListener('DOMContentLoaded', function () {
     
      var el = document.getElementById("query");

      el.onclick = function(tab){ 
          chrome.tabs.executeScript(tab.id, {code:"document.getElementById('fromStationText').value='上海'"});
          chrome.tabs.executeScript(tab.id, {code:"document.getElementById('toStationText').value='北京'"});
          chrome.tabs.executeScript(tab.id, {file: 'ticket.js'});  
      };
});