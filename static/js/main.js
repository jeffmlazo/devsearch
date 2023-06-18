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

let tags = document.querySelectorAll('.project-tag');
for (let i = 0; i < tags.length; i++) {
  tags[i].addEventListener('click', (e) => {
    let tagId = e.target.dataset.tag;
    let projectId = e.target.dataset.project;
    // console.log(`TagID: ${tagId} - projectID: ${projectId}`);

    fetch('http://127.0.0.1:8000/api/remove-tag/', {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ project: projectId, tag: tagId }),
    })
      .then((response) => response.json())
      .then((data) => {
        e.target.remove();
      });
  });
}
