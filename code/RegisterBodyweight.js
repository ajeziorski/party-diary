module.exports.function = function registerBodyweight (bodyweight, bodyweightUnit) {
  var http = require('http');
  var response = http.getUrl("https://ajeziorski.pythonanywhere.com/RegisterBodyweight/" + bodyweightUnit.toLowerCase() + "/" + String(bodyweight), { format: "json", });
  return {ok: true,
          bodyweight: bodyweight,
          bodyweightUnit: bodyweightUnit}
}
