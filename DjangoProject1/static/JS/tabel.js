
document.getElementById('Generate').addEventListener('click',function(){
    var userinput=parseInt(document.getElementById('getinput').value)
    var tabelbody=document.getElementById('tabelbody')
    tabelbody.innerHTML = "";

    for (var i = 1; i <= 10; i++) {
        var result = userinput * i;
        var row = "<tr><td>" + userinput + " x " + i + "</td><td>" + result + "</td></tr>";
        tabelbody.innerHTML += row;
    // console.log(userinput)
    }

})