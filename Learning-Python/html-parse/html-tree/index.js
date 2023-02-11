const BackEndConnection = require('./BackEndConnection');
const backend = BackEndConnection.INSTANCE();

var util = require('util');
var graphviz = require('graphviz');


backend.get_wikipedias_relationships((data) => {
  displayGraphvis(data);
});

function displayGraphvis(relations) {
  var graph = graphviz.digraph("G");

  relations.map(r => r.from_title).forEach(n => {
    graph.addNode(n);
  });

  relations.forEach(r => {
    let fromTitle = r.from_title;
    let toTitle = r.to_title;
    graph.addEdge(fromTitle, toTitle, { "minlen": 2 });
  });;


  graph.setGraphVizPath("/usr/bin");
  graph.output("svg", "/home/tina/Downloads/html-tree.svg");

  let returned_arraye = graph.to_dot();
}