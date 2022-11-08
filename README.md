<!-- Improved compatibility of back to top link: See: https://github.com/jfetff/WinPri/README.md/pull/73 -->
<a name="readme-top"></a>
<!--
*** 
*** 
*** 
*** 
*** 
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/jfetff/WinPri/">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Win 'La Primitiva' using statistics/combinatorics !!</h3>

  <p align="center">
    The Idea of this Project is to create combinations to win 'La Primitiva' in Spain!
    <br />
    <a href="https://github.com/jfetff/WinPri/README.md"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/jfetff/WinPri/README.md">View Demo</a>
    ·
    <a href="https://github.com/othnejfetff/WinPri/README.md/issues">Report Bug</a>
    ·
    <a href="https://github.com/jfetff/WinPri/README.md/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

The main idea of this project is to create different combinations to win La Primitiva. In order to do that we are using all historic combination played so far. Beside that we are using different statiistics and combinatorics methods.

We will be using different files and folders:
* Folders: differents folder to order the use within this project
* Files: We will be using Python, all the code will be implemented .py files
* Other: there will be also some other files and folder needed to understand and keep nice order in the project

We will be adding more information in the near future as the project develops. You may also suggest changes by forking this repo and creating a pull request or opening an issue. Thanks to all the people that could/would contribute expanding this project!


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

The entire project is made usign Python language framework. All the calculation are done using combinatorics. The framework upon which all the execution for this project is done in Visual Studio Code.

* [![Combinatorics][Combinatorics]][Combinatorics-url]
* [![Visual Studio][Visual Studio Code]][Visual Studio Code-url]
* [![Python][Python]][Python-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Independent Python files

1. archivos.py

This python file consists of the following functions:
- a main.py which start the execution of this file
- iniciar() is the function that runs the main function. This function creates all possible combinations 49C2, 49C3, 49C4, 49C5 y 49C6 and then saving them in corresponding Comb-49CX.csv, where X is 2, 3, 4, 5, o 6. These files are archives in the folder ./templates/. Once this function is executed, we need to run it again since the results are stored in files and there will be no changes done in them.





<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

This is guide for instructions on setting up this project locally. In order to that you just need to clone this project and then run it using Visual Studio Code.
To get a local copy up and running follow these simple example steps.

### Prerequisites

The following frameworks are need to build, restore and run this project. All these need to be installed locally.

1. Visual Studio Code
2. Git
3. Python
4. An account in GitHub.com


### Installation

_Below is an example of how you can instruct your audience on installing and setting up your project. This template doesn't rely on any external dependencies or services._

1. Open Visual Studio Code locally
2. Clone the repo
   ```sh
   git clone https://github.com/jfetff/WinPri.git
   ```
3. Open a terminal in Visual Studio Code
   ```sh

   ```
4. Run the correspondent python file `archivos.py`
   ```js

   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

You can find some combinations made using this project. The combinations are located in the folder './tirajes/'. To bet in 'La Primitiva' a person choose 6 numbers from a total of 49. That is called a bet. A bet cost one euro. In one loto ticket is possible to bet up to 8 bets. That is why all the combinations made in this project are put together in groups of 8. The total number of bets that this project creates, depends on how the code is choosing the numbers usign combinatorics.

_For a specific example of the combinations created, please refer to the [./tirajes](https://github.com/jfetff/WinPri.git/tirajes)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Add Changelog
- [x] Add back to top links
- [ ] Add Additional Templates w/ Examples
- [ ] Add "components" document to easily copy & paste sections of the readme
- [ ] Multi-language Support
    - [ ] Chinese
    - [ ] Spanish

See the [open issues](https://github.com/jfetff/WinPri/README.md/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/jfetff/WinPri](https://github.com/jfetff/WinPri)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/jfetff/WinPri/README.md.svg?style=for-the-badge
[contributors-url]: https://github.com/jfetff/WinPri/README.md/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/jfetff/WinPri/README.md.svg?style=for-the-badge
[forks-url]: https://github.com/jfetff/WinPri/README.md/network/members
[stars-shield]: https://img.shields.io/github/stars/jfetff/WinPri/README.md.svg?style=for-the-badge
[stars-url]: https://github.com/jfetff/WinPri/README.md/stargazers
[issues-shield]: https://img.shields.io/github/issues/jfetff/WinPri/README.md.svg?style=for-the-badge
[issues-url]: https://github.com/jfetff/WinPri/README.md/issues
[license-shield]: https://img.shields.io/github/license/jfetff/WinPri/README.md.svg?style=for-the-badge
[license-url]: https://github.com/jfetff/WinPri/README.md/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/jfetff/WinPri
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Visual Studio Code]: https://img.shields.io/badge/Visual%20Studio%20Code-Runs%20everywhere-blue
[Visual Studio Code-url]: https://code.visualstudio.com/
[Python]: https://img.shields.io/badge/Python-Runs%20everywhere-brightgreen
[Python-url]: https://www.python.org/
[Combinatorics]: https://img.shields.io/badge/Combinatorics-Mathematics-blueviolet
[Combinatorics-url]: https://es.mathigon.org/world/Combinatorics/
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
