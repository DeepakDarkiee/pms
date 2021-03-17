<script type="text/javascript">
    $(document).ready(function(){
        $('#period').change(function(){
            var period=this.value;
            var start_date= new Date($('#PMDate').val());
            console.log(start_date);
            if(period=='Annually'){
                var result_date=new Date(start_date.getFullYear()+1, start_date.getMonth(), start_date.getDate());
                result_date=moment(result_date).format('Y-MM-DD');
                $('#NPMDate').val(result_date);

            }
            else if(period=='Monthly'){
                var result_date=new Date(start_date.getFullYear(), start_date.getMonth()+1, start_date.getDate());
                result_date=moment(result_date).format('Y-MM-DD');
                $('#NPMDate').val(result_date);
            }
            else if(period=='Quarterly'){
                var result_date=new Date(start_date.getFullYear(), start_date.getMonth()+3, start_date.getDate());
                result_date=moment(result_date).format('Y-MM-DD');
                $('#NPMDate').val(result_date);
            }
            else if(period=='HalfYear'){
                var result_date=new Date(start_date.getFullYear(), start_date.getMonth()+6, start_date.getDate());
                result_date=moment(result_date).format('Y-MM-DD');
                $('#NPMDate').val(result_date);
            }
            else if(period=='OneTime'){

                var result_date="00-00-00";
                result_date=moment(result_date).format('Y-MM-DD');
                $('#NPMDate').val(result_date);
            }
        })
    });
</script>

<script type="text/javascript">
  $(document).ready(function(){
      $('#PMDate').change(function(){
        
        
          var start_date= new Date(this.value);
          
          var period= new $('#period').val();

          

          console.log(start_date);
          if(period=='Annually'){
              var result_date=new Date(start_date.getFullYear()+1, start_date.getMonth(), start_date.getDate());
              result_date=moment(result_date).format('Y-MM-DD');
              $('#NPMDate').val(result_date);
              
          }
          else if(period=='Monthly'){
            
              var result_date=new Date(start_date.getFullYear(), start_date.getMonth()+1, start_date.getDate());
            console.log(result_date);
              result_date=moment(result_date).format('Y-MM-DD');
              $('#NPMDate').val(result_date);
          }
          else if(period=='Quarterly'){
              var result_date=new Date(start_date.getFullYear(), start_date.getMonth()+3, start_date.getDate());
              result_date=moment(result_date).format('Y-MM-DD');
              $('#NPMDate').val(result_date);
          }
          else if(period=='HalfYear'){
              var result_date=new Date(start_date.getFullYear(), start_date.getMonth()+6, start_date.getDate());
              result_date=moment(result_date).format('Y-MM-DD');
              $('#NPMDate').val(result_date);
          }
           else if(period=='OneTime'){
                var result_date="00-00-00"
                result_date=moment(result_date).format('Y-MM-DD');
                $('#NPMDate').val(result_date);
            }
      })
  });
</script>