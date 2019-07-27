      




  $(".costum-modal").find("input").addClass("form-control");
      
      $(".costum-modal").find("button[type=submit]").click(function (event) {
        event.preventDefault();
        let modalLink    = String(this.getAttribute("modal"));
        let modalElement = $("#" + String(this.getAttribute("modal")));
        console.log(String(this.getAttribute("modal")));
        modalElement.css({"opacity":"0.8"});
        let spinner     = modalElement.parent().find(".costum-modal-spinner-container");
        console.log(spinner);
        spinner.show();
        
        var protocol    = location.protocol;
        var slashes     = protocol.concat("//");
        var host        = slashes.concat(window.location.hostname);
        host            += ":" + window.location.port;
        let endPoint    = this.getAttribute("endpoint");
        let formData    = $(this.parentElement.parentElement.parentElement).serialize();
        $.ajax(
          {
            url: host + endPoint, 
            method:"POST",
            data:formData,
            success: function(resulte){
            console.log("mriiigla belmsak",resulte);
            
            $("#confirmation-modal").find(".costum-modal-body").html("Merci pour votre soumission vous sera contacté ultérieurement ");
            modalElement.css({"opacity":"1"});
            spinner.hide();
            closeModal(modalLink);
            openModal("confirmation-modal",null,"req-success");
            

            
            },
            error:function (err) {
              console.log("the err is ",err);
              modalElement.css({"opacity":"1"});
              spinner.hide();
              closeModal(modalLink);
              $("#confirmation-modal").find(".costum-modal-body").html("une erreur inattendue s'est produite. veuillez vérifier la conformité de vos informations réessayer ultérieurement");
              console.log($("#confirmation-modal").find(".costum-modal-body").innerHtml);
              openModal("confirmation-modal",null,"req-failed");
            }
          });
      });
      function getBodyEvent(event) {
  
        let modalLink   = $("body").attr('modal');
        let keyCode     = event.keyCode;
        if (keyCode == 27) closeModal(modalLink);
      }
      function getTriggeredElement(element,event){
        let x     = event.target.className;
        if ( x.search("modal-in-the-show")>0 )  
          {
           closeModal(element.firstElementChild.id); 
          }
      }

      $(".modal-trigger").click(function (){
        
          let modalLink = this.getAttribute("modal");
          let endPoint  = this.getAttribute("endpoint");
          if (endPoint) openModal(modalLink,endPoint)
          else openModal(modalLink);
          
      });
      $(".modal-dismiss").click(function (event){
          event.preventDefault();
          let modalLink = this.getAttribute("modal");
          closeModal(modalLink);
      });

      
      


      function openModal(modalLink,endpoint=null,className=null) {
        let modalElement    = $("#" + String(modalLink));
        let modalContainer  = modalElement.parent();

        if (className) modalElement.attr("class",className + " costum-modal container col-10 col-sm-8 col-md-5");
        modalContainer.fadeIn(300);
        if (endpoint) modalElement.find("button[type=submit]").attr("endpoint",endpoint);
        modalElement.fadeIn("slow");
        modalContainer.toggleClass("modal-in-the-show");
        $("body").attr('onkeydown','getBodyEvent(event);');
        $("body").attr('modal',String(modalLink));
      }


      function closeModal(modalLink) {
        let modalElement    = $("#" + String(modalLink));
        let modalContainer  = modalElement.parent();
        modalElement.fadeOut(300);
        $("body").removeAttr('onkeydown');
        $("body").removeAttr('modal');
        modalContainer.fadeOut(250);
          setTimeout(
            function() 
            {
              modalContainer.toggleClass("modal-in-the-show");
            }, 600);
        modalElement.css("display","none");
      }

      



      