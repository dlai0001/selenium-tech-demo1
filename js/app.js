App = Ember.Application.create();

App.Router.map(function() {
  // put your routes here
    this.route("movebox", { path: "/movebox"});
    this.route("livesearch", { path: "/livesearch"});
});

App.Store = DS.Store.extend({
    adapter: DS.FixtureAdapter.create()
});


App.IndexRoute = Ember.Route.extend({
  model: function() {
    return App.Person.find();
  }
});


App.LivesearchRoute = Ember.Route.extend({
    model:function() {
        return App.Person.find();
    }
});


App.IndexController = Ember.ArrayController.extend({
   itemSelected: function(item) {
       console.log("clicked on:", item.get('fullName'));
       item.set('isSelected', !item.get('isSelected'));
   },


    sortAscending: false,
    sortProperties:['moneyRaised']

});


App.MoveboxController = Ember.ObjectController.extend({
    purchased: false,
    buyMe: function() {
        this.set('purchased', true);
    }
})

App.LivesearchController = Ember.ArrayController.extend({

    searchValue: '',

    searchTrigger: 0,

    filteredContent: function() {
        searchString = this.get('searchValue');

        //Ajax delay simulation


        var content = this.get('content');

        if(searchString.length > 0) {
            return content.filter(function(item){
                return item.get('fullName').indexOf(searchString) >= 0;
            });
        } else {
            return content;
        }
    }.property('searchTrigger'),


    delaySearch: function() {
        console.log("LATCH UNSET");
        window._AUTOMATION_LATCH = false;
        _this = this
        Ember.run.debounce({name:'livesearch'}, function() {

            //------------------------------------------------------------------
            // Notice JQuery ajax calls return Promise objects.
            //------------------------------------------------------------------
            var jqxhr = $.get("http://google.com", function() {
            })
            .always(function() {
                console.log("ajax round trip completed.");
                // dev code that does ajax processing.
                _this.incrementProperty('searchTrigger');

            }).always(function(){
                //------------------------------------------------------------------
                // Notice I just daisy chain my LATCH unto the ajax promise object.
                //------------------------------------------------------------------
                console.log("LATCH SET");
                window._AUTOMATION_LATCH = true;
            });


        }, 1000);
    }.observes('searchValue'),

    sortAscending: false,
    sortProperties:['moneyRaised']



});


App.IndexView = Ember.View.extend({
    interval: null,

    didInsertElement: function(){
        var myinterval = setInterval(function(){
            pid = Math.floor(Math.random()*6) + 1;
            money = Math.floor(Math.random()*500) / 100;
            App.Person.find(pid).incrementProperty('moneyRaised', money);
        }, 4);
        this.set('interval', myinterval)
    },

    willDestroyElement: function() {
        clearInterval(this.get('interval'))
    }
});

App.MoveboxView = Ember.View.extend({
    didInsertElement: function() {
        var view = this
        this.$("#ccSlideOut").hide();

        this.$("#buybutton").click(
            function(){
                view.$("#ccSlideOut").slideDown(2000, function() {
                    try{
                        console.log("slide in complete");
                        view.get('controller').send('slideInComplete');
                    }catch(e){console.log(e);}
                });
            }
        );

    }

})


App.Person = DS.Model.extend({
    firstName: DS.attr('string'),
    lastName: DS.attr('string'),
    birthday: DS.attr('date'),
    isSelected: DS.attr('boolean'),
    moneyRaised: DS.attr('number'),

    formatMoney:function() {
        return this.get('moneyRaised').toFixed(2);
    }.property('moneyRaised'),

    fullName: function() {
        return this.get('firstName') + ' ' + this.get('lastName');
    }.property('firstName', 'lastName')


});



App.Person.FIXTURES = [
    { id: 1, firstName: 'Trek', lastName: 'Glowacki', moneyRaised:0 },
    { id: 2, firstName: 'Bob', lastName: 'Sanders', moneyRaised:0 },
    { id: 3, firstName: 'George', lastName: 'Thompson', moneyRaised:0 },
    { id: 4, firstName: 'Scott', lastName: 'McKinly', moneyRaised:0 },
    { id: 5, firstName: 'Albert', lastName: 'Einstein', moneyRaised:0 },
    { id: 6, firstName: 'Tom' , lastName: 'Dale', moneyRaised:0 }
];


