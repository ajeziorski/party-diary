module.exports.function = function requestBAC () {
  var BACValue = 5;
  var BACError = 2;
  return {ok: true, 
          BACValue: BACValue, 
          BACError: BACError}
}
