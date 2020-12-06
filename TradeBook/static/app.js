
new Vue({
    el: '#category',
    data: {
        categories: []
             },
    created: function (){
      const vm = this;
      axios.get('/api/categories/').then(function (response) {
        vm.categories = response.data
      })
    }
}

)