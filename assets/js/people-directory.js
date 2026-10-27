/* People page (/people/): tidies the auto-generated board and member entries and adds
   search + topic filters. Without JavaScript the page still shows the plain lists.

   Each generated entry looks like:
   <div class="content" data-tags="A,B">
     <p>[<img> (board only)]
        <span title="bio"><strong>Name, Role, Organisation</strong></span><br>
        Topic A * Topic B * <a>Publications (Scholar)</a> * <a>ORCID</a></p>
   </div>
*/
(function () {
  var MIN_TOPIC = 10; // topics with at least this many people get a filter button

  var LINKS = [
    { match: /scholar/i, icon: 'fab fa-google-scholar', label: 'Publications (Google Scholar)' },
    { match: /orcid/i, icon: 'fab fa-orcid', label: 'ORCID' },
    { match: /research group/i, icon: 'fas fa-users', label: 'Research group' },
    { match: /profile|more info/i, icon: 'fas fa-user', label: 'Researcher profile' },
    { match: /bluesky/i, icon: 'fab fa-bluesky', label: 'Bluesky' },
    { match: /linkedin/i, icon: 'fab fa-linkedin', label: 'LinkedIn' },
    { match: /github/i, icon: 'fab fa-github', label: 'GitHub' }
  ];

  var entries = Array.prototype.slice.call(document.querySelectorAll('.people-board .content, .people-list .content'));
  if (!entries.length) return;

  function el(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text) e.textContent = text;
    return e;
  }

  var people = entries.map(function (div) {
    var p = div.querySelector('p') || div;
    var img = p.querySelector('img');
    var strong = p.querySelector('strong');
    var bio = (p.querySelector('span[title]') || {}).title || '';
    var full = strong ? strong.textContent.trim() : '';
    var cut = full.indexOf(', ');
    var name = cut > 0 ? full.slice(0, cut) : full;
    var role = cut > 0 ? full.slice(cut + 2) : '';

    // text after the <br>: topics (plain text) and links, separated by " * "
    var topics = [], links = [], afterBr = false;
    Array.prototype.forEach.call(p.childNodes, function (n) {
      if (n.nodeName === 'BR') { afterBr = true; return; }
      if (!afterBr) return;
      if (n.nodeName === 'A') links.push(n);
      else if (n.nodeType === 3) {
        n.textContent.split('*').forEach(function (t) { t = t.trim(); if (t) topics.push(t); });
      }
    });
    var tags = (div.getAttribute('data-tags') || '').split(',')
      .map(function (t) { return t.trim(); }).filter(Boolean);

    // rebuild the entry
    var out = document.createDocumentFragment();
    if (img) { img.classList.add('people-entry__photo'); out.appendChild(img); }
    var head = el('span', 'people-entry__head');
    if (bio) head.title = bio; // bio stays a hover tooltip
    head.appendChild(el('strong', 'people-entry__name', name));
    if (role) head.appendChild(el('span', 'people-entry__role', role));
    out.appendChild(head);
    if (topics.length) out.appendChild(el('span', 'people-entry__topics', topics.join(' · ')));
    if (links.length) {
      var box = el('span', 'people-entry__links');
      links.forEach(function (a) {
        var text = a.textContent.trim();
        var kind = LINKS.filter(function (k) { return k.match.test(text); })[0];
        var link = el('a');
        link.href = a.href;
        link.rel = 'noopener';
        link.title = kind ? kind.label : text;
        link.setAttribute('aria-label', (kind ? kind.label : text) + ' – ' + name);
        link.appendChild(el('i', kind ? kind.icon : 'fas fa-link'));
        link.firstChild.setAttribute('aria-hidden', 'true');
        box.appendChild(link);
      });
      out.appendChild(box);
    }
    p.textContent = '';
    p.appendChild(out);
    div.classList.add('people-entry');

    return {
      div: div,
      tags: tags,
      text: [full, bio, topics.join(' '), tags.join(' ')].join(' ').toLowerCase()
    };
  });

  // topic buttons: the most common topics, most common first
  var counts = {};
  people.forEach(function (x) { x.tags.forEach(function (t) { counts[t] = (counts[t] || 0) + 1; }); });
  var topics = Object.keys(counts).filter(function (t) { return counts[t] >= MIN_TOPIC; })
    .sort(function (a, b) { return counts[b] - counts[a] || a.localeCompare(b); });

  var bar = document.getElementById('people-topics');
  var search = document.getElementById('people-search');
  var count = document.getElementById('people-count');
  var empty = document.getElementById('people-empty');
  var active = 'all';
  // bios are hover tooltips, so only mention them on devices with a mouse
  var canHover = window.matchMedia && window.matchMedia('(hover: hover)').matches;

  function addButton(value, label) {
    var b = el('button', 'list-filter' + (value === 'all' ? ' is-active' : ''), label);
    b.type = 'button';
    b.setAttribute('data-topic', value);
    b.setAttribute('aria-pressed', value === 'all' ? 'true' : 'false');
    bar.appendChild(b);
  }
  addButton('all', 'All topics');
  topics.forEach(function (t) { addButton(t, t); });

  // section headings ("Board", "Affiliates", ...) hide when nothing below them matches
  var headings = Array.prototype.slice.call(document.querySelectorAll('.people-board h2, .people-list h2'));

  function apply() {
    var q = search.value.trim().toLowerCase();
    var words = q ? q.split(/\s+/) : [];
    var shown = 0;
    people.forEach(function (x) {
      var ok = (active === 'all' || x.tags.indexOf(active) !== -1) &&
        words.every(function (w) { return x.text.indexOf(w) !== -1; });
      x.div.hidden = !ok;
      if (ok) shown++;
    });
    headings.forEach(function (h) {
      var any = false, n = h.nextElementSibling;
      while (n && n.tagName !== 'H2') { if (n.classList.contains('content') && !n.hidden) { any = true; break; } n = n.nextElementSibling; }
      h.hidden = !any;
    });
    count.textContent = (q || active !== 'all')
      ? shown + ' of ' + people.length + ' people match'
      : 'Showing all ' + people.length + ' people listed.' + (canHover ? ' Hover over a name to read their bio.' : '');
    empty.hidden = shown > 0;
  }

  bar.addEventListener('click', function (e) {
    var b = e.target.closest('button');
    if (!b) return;
    active = b.getAttribute('data-topic');
    Array.prototype.forEach.call(bar.children, function (x) {
      var on = x === b;
      x.classList.toggle('is-active', on);
      x.setAttribute('aria-pressed', on ? 'true' : 'false');
    });
    apply();
  });
  search.addEventListener('input', apply);

  document.getElementById('people-filter').hidden = false;
  apply();
})();
