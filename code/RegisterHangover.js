module.exports.function = function registerBodyweight (hangoverRating) {
  var http = require('http');
  var response = http.getUrl("https://ajeziorski.pythonanywhere.com/RegisterHangover/" + String(hangoverRating), { format: "json", });
  return {ok: true,
          hangoverRating: hangoverRating}
}
