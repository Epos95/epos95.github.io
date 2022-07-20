# My blog / home page 

## How to use:
1. Write a org document *somewhere*
2. Use `epos/blog-publish` in emacs to export the org document as HTML to `~/Blog/templates` where it will be stored
3. Building the project with `just build` or `just run` will generate the finished articles out of those stored in `~/Blog/templates` and put the in the project root for github pages to reach
4. After this `just publish` can be used to push the new generated articles to github.
5. Now the articles should be available on the [blog](https://epos95.github.io/)

