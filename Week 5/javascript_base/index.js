function onmousing(x) {
    x.style.background = 'red';
    x.innerText = 'Some awesome text!'


}

function alerting(x) {
    alert('Click on the button instead!')
}

function outkey(x) {
    x.style.background = 'blue';
    x.innerText = '';
}

var button = function () {
    var but = document.getElementById('hidden');
    but.style.visibility = 'visible';
}





