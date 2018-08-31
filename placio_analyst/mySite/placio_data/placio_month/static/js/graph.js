window.onload = function () {
    var dps=[];
    var chart = new CanvasJS.Chart("chartContainer", {
      animationEnabled: true,
      exportEnabled: true,
      theme: "light1", // "light1", "light2", "dark1", "dark2"
      title:{
        text: "Simple Column Chart with Index Labels"
      },
      data: [{
        type: "column", 
        indexLabelFontColor: "#5A5757",
        indexLabelPlacement: "outside",
        dataPoints: dps
      }]
    });
      

      function addDataPointsAndRender() {
        xValue = Number(document.getElementById('x-value').value);
        yValue = Number(document.getElementById('y-value').value);
        dps.push({
            x: xValue,
            y: yValue
        });
        chart.render();
    }
     
    var renderButton = document.getElementById('renderButton');
    renderButton.addEventListener('click', addDataPointsAndRender);
}