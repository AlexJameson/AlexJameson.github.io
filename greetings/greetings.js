$(function () {
    $("#accordion").dxAccordion({
        dataSource: accordionData,
        multiple: true,
        collapsible: true,
        selectedItems: [accordionData[0]],
        itemTemplate: function (itemData, itemIndex, itemElement) {
            itemElement.append("<p>" + itemData.topic1 + "&nbsp;</p>");
            if (itemData.topic2) {
                itemElement.append("<p>" + itemData.topic2 + "&nbsp;</p>");
            }
            if (itemData.topic3) {
                itemElement.append("<p>" + itemData.topic3 + "</p>");
            }
            
        },
        itemTitleTemplate: function (itemData, itemIndex, itemElement) {
            itemElement.append("<span>" + itemData.title + "&nbsp;</span> ");
        }
    });

    
    const drawer = $("#drawer").dxDrawer({
        height: 600,
        closeOnOutsideClick: true,
        template: function() {
            var $list = $("<div>").width(200).addClass("panel-list");

            return $list.dxList({
                items: accordionData,
                displayExpr: "title",
                hoverStateEnabled: false,
                focusStateEnabled: false,
                activeStateEnabled: false
            });
        }
    }).dxDrawer("instance");

    $("#toolbar").dxToolbar({
        items: [{
            widget: "dxButton",
            location: "before",
            options: {
                icon: "menu",
                text: "Contents",
                onClick: function() {
                    drawer.toggle(); 
                }
            }
        }]
    });
});
