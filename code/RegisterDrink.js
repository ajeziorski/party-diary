module.exports.function = function registerDrink (drinkType, drinkPercentage) {
  var http = require('http');
  if (drinkPercentage == -1)
    {
      var registeredPercentage = 5
    }
  else
    {
      var registeredPercentage = drinkPercentage;
    }
  var response = http.getUrl("https://ajeziorski.pythonanywhere.com/RegisterDrink/" + drinkType.toLowerCase() + "/" + String(registeredPercentage), { format: "json", });
  return {ok: true,
         drinkType: drinkType,
         drinkPercentage: drinkPercentage}
}
