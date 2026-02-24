# git workflow with Django counter app
## For every step in the guide apply the respective git commands (updated)

  1. Fork this repo
  2. Clone your forked repo (1 and 2 one command):
     
      `gh repo fork y44k0v/comIT-py4web26-1-git-django-counter --clone`

  3. Create a folder named after yourself
     
      `mkdir tim`
     
  4. Exit the cloned repo

      `cd ..`
   
  5. Build the app with the instructions bellow and the guide.
     
     "SETUP_GUIDE_HTMX.md"


Track changes, add files, commit changes, once the app running create a new branch: 

    git checkout -b my_counter 
     (any other name works too)
     
  6. Edit:
  * DaisyUI Theme - line 2 `django-counter-app/counter/templates/counter/index.html`
    pick one from the list of [themes](https://daisyui.com/docs/themes/)
  * Card title adding your name after the first ">" - line 19 `django-counter-app/counter/templates/counter/index.html`
    
    ```
       git add .
       git commit -m " Personilize app"
    ```
  7. Switch back to main branch and merge the previous branch.

     
  `git checkout main`
  `git merge my_counter`
    
  9. Take a screenshot of your git log, and the app running.
  10. Create a markdown file inside the folder with your name in the cloned repo, add a title and small description, include your pictures there.
  11. Submit a pull request.
