/* "Load more" for long card lists (/news/, past events, past job openings, ...).
   Mark a grid with data-load-more="12": only the first 12 cards show, and a button
   below reveals 12 more at a time. Hidden cards don't fetch their (lazy) images.
   Without JavaScript every card shows, as before.

   Filters (the chips on /news/) mark cards with data-filtered-out and then call
   grid.loadMoreRefresh(), which starts again from the first page of matching cards.
*/
(function () {
  var grids = document.querySelectorAll('[data-load-more]');

  Array.prototype.forEach.call(grids, function (grid) {
    var step = parseInt(grid.getAttribute('data-load-more'), 10) || 12;
    var limit = step;
    var items = Array.prototype.slice.call(grid.children);

    var wrap = document.createElement('div');
    wrap.className = 'load-more';
    var button = document.createElement('button');
    button.type = 'button';
    button.className = 'home-btn home-btn--outline load-more__btn';
    var status = document.createElement('p');
    status.className = 'load-more__status';
    status.setAttribute('aria-live', 'polite');
    wrap.appendChild(status);
    wrap.appendChild(button);
    grid.parentNode.insertBefore(wrap, grid.nextSibling);

    function matching() {
      return items.filter(function (c) { return !c.hasAttribute('data-filtered-out'); });
    }

    function update() {
      var total = matching().length;
      // don't leave a handful behind a button: show them straight away
      var max = total - limit <= step / 2 ? total : limit;
      var shown = 0;
      items.forEach(function (c) {
        var ok = !c.hasAttribute('data-filtered-out') && shown < max;
        if (ok) shown++;
        c.hidden = !ok;
      });
      var left = total - shown;
      wrap.hidden = left <= 0;
      status.textContent = 'Showing ' + shown + ' of ' + total;
      button.textContent = 'Load ' + Math.min(step, left) + ' more';
    }

    button.addEventListener('click', function () {
      var firstNew = matching()[limit];
      limit += step;
      update();
      // keyboard users continue from the first newly shown card
      var link = firstNew && firstNew.querySelector('a[href]:not([tabindex="-1"])');
      if (link) link.focus({ preventScroll: true });
    });

    grid.loadMoreRefresh = function () { limit = step; update(); };
    update();
  });
})();
