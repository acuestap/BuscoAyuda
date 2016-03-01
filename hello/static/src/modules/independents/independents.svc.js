(function (ng) {
    var mod = ng.module('independentsModule');

    /*mod.config(function($httpProvider, $cookies){
        $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
    })*/
    mod.service('fileUpload', ['$http', 'independentsContext', function ($http, context) {
        this.uploadFileToUrl = function(file, uploadUrl){
            var fd = new FormData();
            fd.append('file', file);
            $http.post(uploadUrl, fd, {
                transformRequest: angular.identity,
                headers: {'Content-Type': undefined}
            })
            .success(function(){
            })
            .error(function (){
            });
        }
    }]);

    mod.service('independentsService', ['$http', 'independentsContext', function ($http, context) {

        this.getIndependents = function () {
            return $http({
                method: 'GET',
                url: '/independents'
            });
        };

        this.registerIndependent = function (data) {
            return $http({
                method: 'POST',
                url: '/register',
                data:data
            });
        };

        this.getJobs = function () {
            return $http({
                method: 'GET',
                url: '/jobs'
            });
        };
    }]);
    
})(window.angular);