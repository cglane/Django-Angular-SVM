MainService.$inject = ['$http','$rootScope'];
export default function MainService($http,$rootScope){
  var MainService = {
    getUsers : getUsers,
    getFiles : getFiles,
    saveFile: saveFile
  };

  return MainService;

  function getUsers(){
    return $http.get('api/users')
  }
  function getFiles(){
    return $http.get('api/train_data')
  }
  function saveFile(file,csrftoken){
    return $http.post('api/train_data',file,{
      headers: {'Content-Type': undefined,"X-CSRFToken": csrftoken},
      transformRequest: angular.identity
    })
  }
}
