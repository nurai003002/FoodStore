! function(e) {
    // var parent = document.querySelectorAll("[data-hover='fancyHover']");
    e.fn.mouseHover = function() {
        var parent = jQuery(this);
        Array.from(parent).forEach(element => {
            if (element) {
                element.insertAdjacentHTML('beforeend', '<span class="target"></span>')
                const links = element.querySelectorAll(".hover-effect");
                const target = element.querySelector(".target");
                function mouseenterFunc() {
                    const width = this.offsetWidth;
                    const height = this.offsetHeight;
                    const left = this.offsetLeft;
                    const top = this.offsetTop;
                    const radius = getComputedStyle(this);
                    target.style.width = `${width}px`;
                    target.style.height = `${height}px`;
                    target.style.left = `${left}px`;
                    target.style.top = `${top}px`;
                    target.style.transform = "none";
                    target.style.borderRadius = radius.getPropertyValue('border-radius');
                    if (!this.parentNode.classList.contains("active")) {
                        for (let i = 0; i < links.length; i++) {
                            if (links[i].parentNode.classList.contains("active")) {
                                links[i].parentNode.classList.remove("active");
                            }
                        }
                        this.parentNode.classList.add("active");
                    }
                }
                for (let i = 0; i < links.length; i++) {
                    links[i].addEventListener("click", (e) => e.preventDefault());
                    links[i].addEventListener("mouseenter", mouseenterFunc);
                    links[i].addEventListener("click", mouseenterFunc);
                }
            }
        });
    }
}(jQuery);

// (function() {
//     function mouseHover(fancyHover) {
//         var parent = fancyHover;
//         parent.forEach(function(element) {
//             if (element) {
//                 element.insertAdjacentHTML('beforeend', '<span class="target"></span>');
//                 var links = element.querySelectorAll(".hover-effect");
//                 var target = element.querySelector(".target");
//                 function mouseenterFunc() {
//                     var width = this.offsetWidth;
//                     var height = this.offsetHeight;
//                     var left = this.offsetLeft;
//                     var top = this.offsetTop;
//                     var radius = getComputedStyle(this).getPropertyValue('border-radius');
//                     target.style.width = width + "px";
//                     target.style.height = height + "px";
//                     target.style.left = left + "px";
//                     target.style.top = top + "px";
//                     target.style.transform = "none";
//                     target.style.borderRadius = radius;
//                     if (!this.parentNode.classList.contains("active")) {
//                         Array.from(links).forEach(function(link) {
//                             if (link.parentNode.classList.contains("active")) {
//                                 link.parentNode.classList.remove("active");
//                             }
//                         });
//                         this.parentNode.classList.add("active");
//                     }
//                 }
//                 Array.from(links).forEach(function(link) {
//                     link.addEventListener("click", function(e) {
//                         e.preventDefault();
//                     });
//                     link.addEventListener("mouseenter", mouseenterFunc);
//                     link.addEventListener("click", mouseenterFunc);
//                 });
//             }
//         });
//     }
//     window.mouseHover = mouseHover;
// })();
