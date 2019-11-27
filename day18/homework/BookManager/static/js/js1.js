setInterval(f, 200);

function f() {
    var content = document.getElementById('content');
    var color = parseInt(Math.ceil(Math.random() * 16777216), 16);
    content.style.color = '#' + color
}