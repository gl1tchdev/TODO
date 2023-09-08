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
let pickr_instance = $("#datetimepicker");
const optional_config = {
    enableTime: true,
    dateFormat: "Y-m-d H:i",
    onChange: function (selectedDates, dateStr, instance) {
        instance.close();
        let input = document.createElement('input');
        input.type = 'hidden';
        input.value = dateStr;
        input.name = 'date_time'
        $('#pickr_area').append(input);
    },
};
pickr_instance.flatpickr(optional_config);

$(function () {
    $("[rel='tooltip']").tooltip();
});

