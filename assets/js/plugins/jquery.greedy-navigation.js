/*
* Greedy Navigation
*
* http://codepen.io/lukejacksonn/pen/PwmwWV
*
*/

var $nav = $('#site-nav');
var $btn = $('#site-nav button');
var $vlinks = $('#site-nav .visible-links');
var $hlinks = $('#site-nav .hidden-links');

var breaks = [];

function updateNav() {

  var availableSpace = $btn.hasClass('hidden') ? $nav.width() : $nav.width() - $btn.width() - 30;

  var $movable = $vlinks.children('*:not(.masthead__menu-item--lg)');

  // The visible list is overflowing the nav (and there is still an item left to hide)
  if($vlinks.width() > availableSpace && $movable.length) {

    // Record the width of the list
    breaks.push($vlinks.width());

    // Move item to the hidden list
    $movable.last().prependTo($hlinks);

    // Show the dropdown btn
    if($btn.hasClass('hidden')) {
      $btn.removeClass('hidden');
    }

  // The visible list is not overflowing
  } else {

    // There is space for another item in the nav
    if(breaks.length && availableSpace > breaks[breaks.length-1]) {

      // Move the item to the visible list
      $hlinks.children().first().appendTo($vlinks);
      breaks.pop();
    }

    // Hide the dropdown btn if hidden list is empty
    if(breaks.length < 1) {
      $btn.addClass('hidden');
      $hlinks.addClass('hidden');
    }
  }

  // Keep counter updated
  $btn.attr("count", breaks.length);

  // Recur if the visible list is still overflowing the nav and something can still be hidden,
  // or if there is still room to bring back more hidden items (e.g. after widening the window).
  // The guards stop endless recursion when nothing is left to move (e.g. on a very narrow phone).
  if($vlinks.width() > availableSpace && $vlinks.children('*:not(.masthead__menu-item--lg)').length) {
    updateNav();
  } else if(breaks.length && $hlinks.children().length && availableSpace > breaks[breaks.length-1]) {
    updateNav();
  }

}

// Window listeners

$(window).resize(function() {
  updateNav();
});

$btn.on('click', function() {
  $hlinks.toggleClass('hidden');
  $(this).toggleClass('close');
});

updateNav();