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
        main.displayImage(event.currentTarget.href);
        return false;
    },
    displayImage: function(src) {
        window.scrollTo(0, 0);
        if (console) console.log("Showing "+src);
        $('#preview-image img').attr('src', src);
    },
    displayNextImage: function(event) {

    }
};

$(function(){main.init();});
