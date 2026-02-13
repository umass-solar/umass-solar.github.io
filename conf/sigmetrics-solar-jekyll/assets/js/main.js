(function(){
  function toggle(){
    var nav = document.getElementById('site-nav');
    if(!nav) return;
    nav.classList.toggle('open');
  }
  window.__toggleNav = toggle;
})();
