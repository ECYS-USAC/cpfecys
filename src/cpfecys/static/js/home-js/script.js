/**
 * ------------------------------------------------------------------------
 * JA University T3 template
 * ------------------------------------------------------------------------
 * Copyright (C) 2004-2011 J.O.O.M Solutions Co., Ltd. All Rights Reserved.
 * @license - Copyrighted Commercial Software
 * Author: J.O.O.M Solutions Co., Ltd
 * Websites:  http://www.joomlart.com -  http://www.joomlancers.com
 * This file may not be redistributed in whole or significant part.
 * ------------------------------------------------------------------------
 */
 (function($){
    $(document).ready(function(){
      //Fix bug tabs
      if($('.nav.nav-tabs').length > 0){
        $('.nav.nav-tabs a').click(function (e) {
                        e.preventDefault();
                        $(this).tab('show');
                    })
      }
      //Check div message show
      (function(){
            if($("#system-message").children().length){
                $("#system-message-container").show();
                $("#system-message a.close").click(function(){
                    setTimeout(function(){
                        if(!$("#system-message").children().length) $("#system-message-container").hide();

                        if($('#t3-content').length >0 && $('#t3-content').html().trim().length == 0){
                            $('#t3-content').hide();
                        }else if($('#t3-content').find('.blog-featured').length>0 && $('#t3-content').find('.blog-featured').html().trim().length == 0 && $("#system-message").children().length == 0){
                            $('#t3-content').hide();
                        }
                    }, 100);
                });
            } else {
                $("#system-message-container").hide();
            }
      })();
	  //Check with submenu
	  (function(){
		  if($('.nav.navbar-nav').find('.nav-child').length){
			$('.nav.navbar-nav').find('.nav-child').each(function(){
				if($(this).width() > $(window).width()) $(this).css('width',$(window).width());
			});
		  }
	  })();
    });
 })(jQuery);