module.exports.function = function requestBAC () {
  var http = require('http');
  var response = http.getUrl("https://ajeziorski.pythonanywhere.com/RequestBAC", { format: "json", });
  return response
}
