/**
 * @ngdoc controller
 * @name gdgSettingsApp.controller:MainCtrl
 * @description
 * List view of the user's clients
 */
MainCtrl.$inject = ['$http', '$timeout','$scope','$state', 'MainService','$rootScope'];
export default function MainCtrl($http, $timeout,$scope,$state, MainService,$rootScope) {
  var vm = this;
  vm.uploadObj = {}

  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

  function init(){
    MainService.getFiles().then(response =>{
      console.log(response,'response');
    })
  }


}
