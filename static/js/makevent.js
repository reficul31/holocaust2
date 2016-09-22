$(document).ready(function() {

    $(document).on('click', '.add-form-option-textbox', function() {
        $('.add-form-fields-construct').append('<div class="form-element form-textbox"><span>Textbox</span><input class="form-textbox-label" placeholder="label"><input class="form-textbox-placeholder" placeholder="placeholder"></div>'); 
        });

    $(document).on('click', '.add-form-option-checkbox', function() {
        $('.add-form-fields-construct').append('<div class="form-element form-checkbox"><span>Checkbox</span><input class="form-checkbox-label" placeholder="label"><input class="form-checkbox-values" placeholder="comma separated values"></div>'); 
        });

    $(document).on('click', '.add-form-option-radiobutton', function() {
         $('.add-form-fields-construct').append('<div class="form-element form-radiobutton"><span>Radio Button</span><input class="form-radiobutton-label" placeholder="label"><input class="form-radiobutton-values" placeholder="comma separated values"></div>');
    });

});

$('#send').click(function()
{
    var formdata = {
    eventname: $('.add-form-meta-eventname').val(),
    eventpasskey: $('.add-form-meta-eventpasskey').val(),
    form_data: {
        fields: []
    }
  };

$('.form-element').each(function(index) {
    var field = {};
    if ($(this).hasClass('form-textbox')) {
        field = {
            type: 'textbox',
            label: $(this).children('input').eq(0).val()
        };
    }
    else if ($(this).hasClass('form-checkbox')) {
        field = {
            type: 'checkbox',
            label: $(this).children('input').eq(0).val(),
            vals: $(this).children('input').eq(1).val()
        };
    }
    else if ($(this).hasClass('form-radiobutton')) {
        field = {
            type: 'radiobutton',
            label: $(this).children('input').eq(0).val(),
            vals: $(this).children('input').eq(1).val()
        };
    }
    
    formdata.form_data.fields.push(field);
});

formdata = JSON.stringify(formdata);
document.getElementById('sender').value= formdata
console.log(document.getElementById('sender').value)
$("#senderform").submit()
});