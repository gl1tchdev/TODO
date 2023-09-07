document.querySelectorAll('.form-outline').forEach((formOutline) => {
  new mdb.Input(formOutline).init();
});
document.querySelectorAll('.form-outline').forEach((formOutline) => {
  new mdb.Input(formOutline).update();
});
var granimInstance = new Granim({
   element: '#canvas-basic',
   name: 'granim',
   opacity: [1, 1],
   states : {
       "default-state": {
           gradients: [
               ['#834D9B', '#D04ED6'],
               ['#1CD8D2', '#93EDC7']
           ]
       }
   }
});