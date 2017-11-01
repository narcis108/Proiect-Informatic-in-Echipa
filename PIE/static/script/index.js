window.onscroll = function () {
    sticky()
};

function sticky() {
    var navbar = document.getElementById("nSticky");
    if (document.body.scrollTop > 101 || document.documentElement.scrollTop > 101) {
        navbar.className = "bar" + " card" + " animate-top" + " black";
    } else {
        navbar.className = navbar.className.replace(" card animate-top black", "");
    }
}

function toggle() {
    var x = document.getElementById("mSticky");
    if (x.className.indexOf("show") == -1) {
        x.className += " show";
    } else {
        x.className = x.className.replace(" show", "");
    }
}

// Modal Image Gallery
function onClick(element) {
    document.getElementById("image").src = element.src;
    document.getElementById("modal").style.display = "block";
    document.getElemenById("link_IMDB").setAttribute("href","http://imdb.com");
    var captionText = document.getElementById("caption");
    captionText.innerHTML = element.alt;
    var descriptionText = document.getElementById("description");
    descriptionText.innerHTML = element.alt;

}
