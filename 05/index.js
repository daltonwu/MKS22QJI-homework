var chart = d3.select("#chart");
var bars = chart.selectAll("div").data(delegates).enter();

bars.append("div")
    .text(function(data, i) {
        return states[i] + ": " + delegates[i] + " delegates (" + dates[i] + ")";
    })
    .style("width", function(data, i) {
        return data * 10 + "px";
    })
    .style("background-color", function(data, i) {
        if(i >= 29) {
            return "#777";
        }
        else {
            return "rgb(71, 159, 223)";
        }
    });
