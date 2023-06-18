let loginBtn = document.querySelector('#login-btn');
let logoutBtn = document.querySelector('#logout-btn');
let projectsUrl = 'http://127.0.0.1:8000/api/projects';
let token = localStorage.getItem('token');

if (token) {
  loginBtn.remove();
} else {
  logoutBtn.remove();
}

logoutBtn.addEventListener('click', (e) => {
  e.preventDefault();
  localStorage.removeItem('token');
  window.location =
    'file:///mnt/BackUpAppsInstallations/MyProjexTest/MyDjangoProjexTest/devsearchfrontend/login.html';
});

let getProjects = () => {
  fetch(projectsUrl)
    .then((response) => response.json())
    .then((data) => {
      buildProjects(data);
    });
};

let buildProjects = (projects) => {
  let projectsWrapper = document.querySelector('#projects--wrapper');
  projectsWrapper.innerHTML = '';

  for (let i = 0; i < projects.length; i++) {
    let project = projects[i];
    let projectCard = `
        <div class="project--card">
            <img src="http://127.0.0.1:8000${project.featured_image}" />
            <div>
                <div class="card--header">
                    <h3>${project.title}</h3>
                    <strong class="vote--option" data-vote="up" data-project="${
                      project.id
                    }">&#43</strong>
                    <strong class="vote--option" data-vote="down" data-project="${
                      project.id
                    }">&#8722</strong>
                </div>
                <i>${project.vote_ratio}% Positive feedback</i>
                <p>${project.description.substring(0, 150)}</p>
            </div>
        </div>
    `;
    projectsWrapper.innerHTML += projectCard;
  }
  addVoteEvents();
  //Add an event listener
};

let addVoteEvents = () => {
  let voteBtns = document.querySelectorAll('.vote--option');
  for (let i = 0; i < voteBtns.length; i++) {
    // console.log(voteBtns[i]);
    voteBtns[i].addEventListener('click', (e) => {
      //   let token = localStorage.getItem('token');
      let token =
        'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg5NTI0MDAwLCJpYXQiOjE2ODY5MzIwMDAsImp0aSI6IjBiOWJiMzBlNjk3ZDRkYjg5NDAzZGQ4YjZhNWExNzdlIiwidXNlcl9pZCI6MX0.LhRe0oPCDlZdGvOInLo3SbnEOj_t48I6moxqpQ80htc';
      let vote = e.target.dataset.vote;
      let project = e.target.dataset.project;
      //   console.log(`PROJECT: ${project}, VOTE: ${vote}`);

      fetch(`http://127.0.0.1:8000/api/projects/${project}/vote/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({ value: vote }),
      })
        .then((response) => response.json())
        .then((data) => {
          console.log('Success:', data);
          getProjects();
        });
    });
  }
};

getProjects();
