we have mattermost project our tasks is to develop docs for it.
we use starlghit astro for it.
the goal is to develope docs for it. 
all docs of mattermost was build have e.rst format we convert it to md files and then we use astro to build the docs. 
I have 2 problem with it.
1-the code syntax must be like for exampe :
   1-for link  
         You can [link to another page](/getting-started/).
    2- inline code 
         You can highlight `inline code` with backticks.
    3- for images 
         ![A rocketship in space](../../assets/images/rocket.svg)
    4- for headers 
        ## Introduction

        I can link to [my conclusion](#conclusion) lower on the same page.

        ## Conclusion

        `https://my-site.com/page1/#introduction` navigates directly to my Introduction.

    5- for notes 
         :::note
             Starlight is a documentation website toolkit built with [Astro](https://astro.build/). You can get started with this command:
        :::
    6- for command line 
        ```sh
           npm create astro@latest -- --template starlight
        ```
    7- for tips 
       :::tip[Did you know?]
          Astro helps you build faster websites with [“Islands Architecture”](https://docs.astro.build/en/concepts/islands/).
        :::
    8- for warnings 
       :::caution
        If you are not sure you want an awesome docs site, think twice before using [Starlight](/).
        :::
    9- for danger  
            :::danger
            Your users may be more productive and find your product easier to use thanks to helpful Starlight features.

            - Clear navigation
            - User-configurable colour theme
            - [i18n support](/guides/i18n/)

            :::
    10- for page title and discription :
        ---
            title: Agents context management
            description: Agents context management
        ---
2- for translation to arabic:
   our audiance is arabic people so we must translate all the docs to arabic but keep the technical terms in english not literal translation but in functional and formal way as possible.
   
*** construction ***
we will use the next rules to build the docs:
- we will take care of the design and styles of each page.
- we can  use .mdx instead of .md format in some cases for better experience.
- we will change the style and design of the  docs from english to arabic
- we already have the structure and the content in the original docs.
- we will apply the rules in the original docs.
- we will use the same rules to format the new docs.
- all images in content should be in the same path in the docs.


start  from path -> C:\Users\AB-Hamoud\pro\mattermost-end-user\src\content\docs\access-your-workspace and do it page by page.