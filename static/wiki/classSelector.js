function clickClassSelector() {
    let classSelector = document.getElementById('class-menu');

    if (classSelector.classList.contains('hidden')) {
       classSelector.classList.remove('hidden');
    } else {
        classSelector.classList.add('hidden');
    }
}

function changeClassIcon() {
    if (localStorage.getItem('class')) {
        let icon = document.getElementById('current-class-icon');
        icon.src = staticUrl + "wiki/images/" + localStorage.class + ".png";
    }
}

function setClass(className) {
    localStorage.setItem('class', className);
    changeClassIcon();
    clickClassSelector();
}

changeClassIcon();
