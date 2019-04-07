/* JS Document */

/******************************

[Table of Contents]

1. Vars and Inits
2. Set Header
3. Init Search
4. Init Menu
5. Init Quantity


******************************/

$(document).ready(function () {
  'use strict';

  /* 

	1. Vars and Inits

	*/

  var header = $('.header');
  var hambActive = false;
  var menuActive = false;

  setHeader();

  $(window).on('resize', function () {
    setHeader();
  });

  $(document).on('scroll', function () {
    setHeader();
  });

  initSearch();
  initMenu();
  initQuantity();
  clearCart();
  updateCart();
  /* 

	2. Set Header

	*/

  function setHeader() {
    if ($(window).scrollTop() > 100) {
      header.addClass('scrolled');
    } else {
      header.removeClass('scrolled');
    }
  }

  /* 

	3. Init Search

	*/

  function initSearch() {
    if ($('.search').length && $('.search_panel').length) {
      var search = $('.search');
      var panel = $('.search_panel');

      search.on('click', function () {
        panel.toggleClass('active');
      });
    }
  }

  /* 

	4. Init Menu

	*/

  function initMenu() {
    if ($('.hamburger').length) {
      var hamb = $('.hamburger');

      hamb.on('click', function (event) {
        event.stopPropagation();

        if (!menuActive) {
          openMenu();

          $(document).one('click', function cls(e) {
            if ($(e.target).hasClass('menu_mm')) {
              $(document).one('click', cls);
            } else {
              closeMenu();
            }
          });
        } else {
          $('.menu').removeClass('active');
          menuActive = false;
        }
      });

      //Handle page menu
      if ($('.page_menu_item').length) {
        var items = $('.page_menu_item');
        items.each(function () {
          var item = $(this);

          item.on('click', function (evt) {
            if (item.hasClass('has-children')) {
              evt.preventDefault();
              evt.stopPropagation();
              var subItem = item.find('> ul');
              if (subItem.hasClass('active')) {
                subItem.toggleClass('active');
                TweenMax.to(subItem, 0.3, { height: 0 });
              } else {
                subItem.toggleClass('active');
                TweenMax.set(subItem, { height: 'auto' });
                TweenMax.from(subItem, 0.3, { height: 0 });
              }
            } else {
              evt.stopPropagation();
            }
          });
        });
      }
    }
  }

  function openMenu() {
    var fs = $('.menu');
    fs.addClass('active');
    hambActive = true;
    menuActive = true;
  }

  function closeMenu() {
    var fs = $('.menu');
    fs.removeClass('active');
    hambActive = false;
    menuActive = false;
  }

  /* 

	5. Init Quantity

	*/
  function $$(selector, context) {
    context = context || document;
    var elements = context.querySelectorAll(selector);
    return Array.prototype.slice.call(elements);
  }

  function initQuantity() {
  
    var incButton = $$('#quantity_inc_button');
    var decButton = $$('#quantity_dec_button');

    for (var i = 0; i < incButton.length; i++) {

 
      var inc = $(incButton[i]).attr('class');
      var z = inc.split(" ");
      var dec = $(decButton[i]).attr('class');
      var z2 = dec.split(" ");
 
      inc = $('.' + z[1])
      dec = $('.' + z2[1])

      inc.on('click', function () {

        var im = $(this).attr('class')
        console.log(im);
        var z = im.split(" ");
        var lastChar = z[1].substr(z[1].length - 1);

        var inp = $('.quantity_input' + lastChar)
        var originalVal = inp.val();
        var endVal = parseFloat(originalVal) + 1;
        inp.val(endVal);
      });
      dec.on('click', function () {

        var im = $(this).attr('class')
        var z = im.split(" ");
        var lastChar = z[1].substr(z[1].length - 1);

        var inp = $('.quantity_input' + lastChar)
        var originalVal = inp.val();
        if (originalVal > 0) {
          var endVal = parseFloat(originalVal) - 1;
          inp.val(endVal);
        }
      });
    }
  }

  //Doing clear cart and update cart
  
  function updateCart(){
    $('.update_cart_button').on('click',()=>{
      alert("AWWADS")
      $.ajax({
        type: 'GET',
        url: window.location.href + '/update/',
        success: function(result) {
          alert(result);
        },
        error: function(result) {
          alert('error');
        },
      });
    })
  }
  function clearCart(){
    $('.clear_cart_button').on('click',()=>{
      alert(window.location.href + '/clear/')
      $.ajax({
        type: 'GET',
        url: window.location.href + '/clear',
        success: function(result) {
          alert(result);
        },
        error: function(result) {
          alert('error');
        },
      });
    })
  }
});
