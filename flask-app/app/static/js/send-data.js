function myFunction () {
        //var day = $('#day').val();
        //var month = $('#month').val();
        var age = $('#age').val();
        var number_of_searches = $('#number_of_searches').val();
        var gender = $('#gender').val();
        var signup = $('#signup').val();
        var date = $(".dtpick")[0].value;
        console.log(date);
      $.ajax({
       type: "POST",
       //contentType: "application/json; charset=utf-8",
       url: "/",
       dataType: "json",
       async: true,
       //data: '{"day": "'+day+'", "month": "'+month+'", "age": "'+age+'", "number_of_searches": "'+number_of_searches+'", "gender": "'+gender+'", "signup": "'+signup+'"}'
       data: {
        "age": age,
        "number_of_searches": number_of_searches,
        "gender": gender,
        "signup": signup,
        "date": date
       },

       success: function (data) {
        console.log(data);
       //   var chance = 100 * data["score"];
       //   d3.select("#chancebar")
       //     .attr("width", chance_scale(chance));
       //   d3.select("#percent_text")
       //     .attr("x", chance_scale(chance-5))
       //     .text(chance.toFixed(1) + "%");
        },
        error: function (result) {
          console.log(result);
       }
      })
      } 
