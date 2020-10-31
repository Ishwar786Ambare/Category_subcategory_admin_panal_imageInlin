jQuery(document).ready(function($) {
// (function($) {
    'use strict';
    $(function() {
        var category = $('#id_category');
        var sub_category = $('#id_subcategory');
        if(!category.val()){
            sub_category.hide();
        } else {
            sub_category.show();
            getSubCategories();
        }
        $(category).change(function(){
            sub_category.show();
            getSubCategories();
        });
        function getSubCategories(){
            var v = $("#id_subcategory").val();
            var valueExist = false;
            $.getJSON("/admin/category/getsubcategories/",{id: $(category).val()}, function(j){
            // $.getJSON("{% url 'product:getSubcategory1' %}",{id: $(category).val()}, function(j){
                var options = '<option value="">---------</option>';
                for (var i = 0; i < j.length; i++) {
                    options += '<option value="' + j[i].pk + '">' + j[i].fields.name + '</option>';
                    if(v==j[i].pk){
                        valueExist=true;
                    }
                }
                $("#id_subcategory").html(options);
                if(valueExist){
                    $("#id_subcategory").val(v);
                }
            });
        }
    });
// })(django.jQuery);
});
