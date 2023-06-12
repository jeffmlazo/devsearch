// Get search form and page links
let searchForm = document.querySelector('#search-form');
let pageLinks = document.querySelectorAll('.page-link');

// Check search form exist
if (searchForm) {
  for (let i = 0; pageLinks.length > i; i++) {
    // The "function" keyword is nescessary instead of the arrow key fos the "this.dataset.page" to work
    pageLinks[i].addEventListener('click', function (e) {
      e.preventDefault();

      // Get the data attribute
      let page = this.dataset.page;

      // Add hidden input to form
      searchForm.innerHTML += `<input value=${page} name="page" hidden/>`;

      // Submit form
      searchForm.submit();
    });
  }
}
