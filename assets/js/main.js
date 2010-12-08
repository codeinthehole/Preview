var main = {
    init: function() {
        main.displayInitialImage();
        main.registerEvents();
    },
    displayInitialImage: function() {
        // Show first image in pages array
        if (typeof pages == "undefined") return;
        main.pageIndex = 0;
        main.versionIndex = 0;
        var url = pages[main.pageIndex].versions[main.versionIndex].url;
        main.displayImage(url);
    },
    registerEvents: function() {
        $('#nav a.page_version').click(main.displayClickedVersion);
        $('#nav_next').click(main.displayNextImage);
    },
    displayClickedVersion: function(event) {
        $('#nav a.page_version').css("font-weight", "normal");
        $('#nav span.page_name').css("font-weight", "normal");
	var target = event.currentTarget;
	var pageTargetId = target.id.substr(0,target.id.length-2);
        main.displayImage(target.href);
	$(target).css("font-weight", "bold");
	$('#nav span#' + pageTargetId).css("font-weight", "bold");
        return false;
    },
    displayImage: function(src) {
        window.scrollTo(0, 0);
        $('#preview-image img').attr('src', src);
    },
    displayNextImage: function(event) {

    }
};

$(function(){main.init();});
