'use strict';

/* Controllers */

angular.module('myApp.controllers', []).
    controller('TagCtrl', ['$scope', '$http', function ($scope, $http) {

        $scope.renameTag = function(tagName) {
            var newName = prompt("Enter new tag name");
            if (!newName) {
              return;
            }
            newName = newName.trim();
            $http.put(tagName + "?name=" + newName)
                .success(function () {
                    console.log("rename successful");
                    window.location.reload(true);
                }).error(function() {
                        console.log("rename failed");
                    });
                // TODO: redirect
        };

        $scope.deleteTag = function(tagName) {
            console.log("delete called: " + tagName);
            $http.delete(tagName)
                .success(function () {
                    console.log("delete successful");
                    window.location.reload(true);
                }).error(function() {
                        console.log("delete failed");
                    });
                // TODO: redirect
        };

        $scope.deleteTagRef = function(id) {
            var url = "refs/" + id;
            console.log("delete called: " + url);
            $http.delete(url)
                .success(function () {
                    console.log("delete successful");
                    window.location.reload(true);
                }).error(function() {
                    console.log("delete failed");
                });
            // TODO: redirect
        };
    }]);
