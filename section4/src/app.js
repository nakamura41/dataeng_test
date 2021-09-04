var margin = { top: 10, right: 20, bottom: 30, left: 50 };
var width = 800 - margin.left - margin.right;
var height = 400 - margin.top - margin.bottom;

var svg = d3.select('.chart')
    .append('svg')
    .attr('width', width + margin.left + margin.right)
    .attr('height', height + margin.top + margin.bottom)
    .call(responsivefy)
    .append('g')
    .attr('transform', `translate(${margin.left}, ${margin.top})`);


var url = 'https://api.covid19api.com/country/singapore/status/confirmed?from=2020-03-01T00:00:00Z&to=2021-09-01T00:00:00Z';

d3.json(url, function (err, data) {
    var parseTime = d3.timeParse('%Y-%m-%dT%H:%M:%SZ');
    data.forEach(function (record, index) {
        record.Date = parseTime(record.Date);
        this[index] = { "Date": record.Date, "Cases": record.Cases }
    }, data);

    var xScale = d3.scaleTime()
        .domain([
            d3.min(data, d => d.Date),
            d3.max(data, d => d.Date)
        ])
        .range([0, width]);
    svg
        .append('g')
        .attr('transform', `translate(0, ${height})`)
        .call(d3.axisBottom(xScale).ticks(10));

    var yScale = d3.scaleLinear()
        .domain([
            d3.min(data, d => d.Cases),
            d3.max(data, d => d.Cases)
        ])
        .range([height, 0]);
    svg
        .append('g')
        .call(d3.axisLeft(yScale));

    var line = d3.line()
        .x(d => xScale(d.Date))
        .y(d => yScale(d.Cases))
        .curve(d3.curveCatmullRom.alpha(0.5));

    svg
        .selectAll('.line')
        .data(data)
        .enter()
        .append('path')
        .attr('class', 'line')
        .attr('d', line(data))
        .style('stroke', '#FF9900')
        .style('stroke-width', 2)
        .style('fill', 'none');
});


function responsivefy(svg) {
    // get container + svg aspect ratio
    var container = d3.select(svg.node().parentNode),
        width = parseInt(svg.style("width")),
        height = parseInt(svg.style("height")),
        aspect = width / height;

    // add viewBox and preserveAspectRatio properties,
    // and call resize so that svg resizes on inital page load
    svg.attr("viewBox", "0 0 " + width + " " + height)
        .attr("preserveAspectRatio", "xMinYMid")
        .call(resize);

    // to register multiple listeners for same event type,
    // you need to add namespace, i.e., 'click.foo'
    // necessary if you call invoke this function for multiple svgs
    // api docs: https://github.com/mbostock/d3/wiki/Selections#on
    d3.select(window).on("resize." + container.attr("id"), resize);

    // get width of container and resize svg to fit it
    function resize() {
        var targetWidth = parseInt(container.style("width"));
        svg.attr("width", targetWidth);
        svg.attr("height", Math.round(targetWidth / aspect));
    }
}
