$(function() {
    $("#treeview").dxTreeView({ 
        items: topics,
        //width: 300,
    });
});

var topics = [{
    id: "1",
    text: "Topics",
    expanded: true,
    items: [{
        id: "1_1",
        text: "Greetings and Small Talk",
        expanded: true,
        template: function(itemData, itemIndex, itemElement) {
            itemElement.append("<a href='greetings/greetings.html'>" + itemData.text +"</a>");
        },
        items: [{
            id: "1_1_1",
            text: "Saying Hello and Goddbye",
            html: ""
            /*items: [{
                id: "1_1_1_1",
                text: "Hello"
            }, {
                id: "1_1_1_2",
                text: "Goodbye",
            }]*/
        }, {
            id: "1_1_2",
            text: "Talking about personal days and absences"
        }]

    }, {
        id: "1_2",
        text: "Planning and Review",
        items: [{
            id: "1_2_1",
            text: "Working with the Trello boards"
        }, {
            id: "1_2_2",
            text: "Discussing general issues with workflow"
        }, {
            id: "1_2_3",
            text: "Setting a task, discussing task progress and required time",
        }, {
            id: "1_2_4",
            text: "Planning, Retro, and Review"
        }]

    }, {
        id: "1_3",
        text: "Daily Routine",
        items: [{
            id: "1_3_1",
            text: "Working with Git"
        }, {
            id: "1_3_2",
            text: "Cooperation and Responds"
        }, {
            id: "1_3_3",
            text: "Handling Support Tickets",
        }]
    }, {
        id: "1_4",
        text: "Technical Discussions",
        items: [{
            id: "1_4_1",
            text: "Architecture"
        }, {
            id: "1_4_2",
            text: "Infrastructure"
        }, {
            id: "1_4_3",
            text: "Documentation"
        }, {
            id: "1_4_4",
            text: "Tests"
        }]

    }]
}];