new Chartist.Line('.ct-chart', {
  labels: labels,
  series: values,
}, {
  fullWidth: true,
  chartPadding: {
    right: 40
  }
});
