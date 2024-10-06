# Sky-Wanderer-NASA-Space-Apps
<div align="center">
<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
<br />
[![LinkedIn][linkedin-shield]][linkedin-url1]
[![LinkedIn2][linkedin-shield]][linkedin-url2]
[![LinkedIn3][linkedin-shield]][linkedin-url3]
[![LinkedIn4][linkedin-shield]][linkedin-url4]
[![LinkedIn5][linkedin-shield]][linkedin-url5]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/asanzra/Sky-Wanderer-NASA-Space-Apps">
    <img src="https://www.telemadrid.es/2024/06/04/noticias/madrid/_2676042494_45798373_1300x731.jpg" alt="Logo" width="729" height="411.1875">
  </a>
</div>

<h3 align="center">Sky Wanderer - Exosky!</h3>

  <p align="center">
    NASA International Space Apps Challenge
    <br />
    <a href="https://www.spaceappschallenge.org/nasa-space-apps-2024/challenges/exosky/"><strong>Explore the challenge »</strong></a>
    <br />
    <a href="https://www.spaceappschallenge.org/nasa-space-apps-2024/find-a-team/explorers-of-the-sky/"><strong>Explore our team and project page »</strong></a>
    <br />
    <a href="https://github.com/user-attachments/assets/49a90214-1aa5-4647-beba-91c0dab4ede1">View Demo</a> <!-- UPDATE URL OF DEMO!!!!-->
    <!-- ·
    <a href="https://github.com/asanzra/Sky-Wanderer-NASA-Space-Apps/issues">Report Bug/Request Feature</a> -->
  </p>
</div>





<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#project-title-and-description">Project Title and Description</a></li>
        <li><a href="#built-with">Built With</a></li>
        <li><a href="#Features">Features</a></li>
        <li><a href="#Usage">Usage</a></li>
      </ul>
    </li>
    <li>
        <a href="#Installation Instructions">Installation Instructions</a>
    </li>
    <li><a href="#references">References</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

Our project, "Sky Wanderer" consists in a learning tool fundamentally concieved with the purpose to, not only make scientific data accessible and understandable to a non-technical audience, but also engage the general public with the unknown and encourage them to look beyond. We achieve this objective through awe-inspiring, but at the same time scientifically accurate simulations of unknown night-skies that only existed in each one´s imagination until know. 

### Project Title and Description

<b>Title:</b> Sky Wanderer

<b>Problem Solved:</b>  Nasa SpaceApps 2024 Challenge: Exosky!

<b>Description:</b> 

Our project aims to bring the immensity of space closer to anyone interested in science, astronomy, and space...
We created an interface that first gets specific data from the Gaia Archive through a query. This data refers to the stars that someone would see at the surface of a particular exoplanet, with the stars at the correct coordinates.  Finally, these stars and exoplanets are plotted in Godot with a terrain simulating the surface of a planet. We can request the data from the [Gaia Data Release 3](https://www.cosmos.esa.int/web/gaia/data-release-3) using [ADQL](https://www.ivoa.net/documents/ADQL/20230418/PR-ADQL-2.1-20230418.html#tth_sEc4.6.1). 

This data includes astrophysical parameters and source class probabilities for about 470 million and 1500 million sources, respectively, including stars, galaxies, and quasars. However, on this project we have focused on the position of the stars visible from a position diferent than Earth, that includes:
- The right ascension coordinate for the source in degrees.
- The declination coordinate for the source in degrees.
- The parallax coordinate for the source in arcsecs.
- The magnitude of the source from our point of view. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [Godot](https://www.tensorflow.org/)
* [ADQL](https://www.ivoa.net/documents/ADQL/20230418/PR-ADQL-2.1-20230418.html#tth_sEc4.6.1)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Features

Main feature: transforming equatorial coordinates to cartesian coordinates and modifying the reference system having the desired exoplanet at the origin. Our interface first gets, in real time, specific data from the Gaia Archive through a query. Therefore, every discovery of new celestial object is rendered in our app. 

The visor provides a clearer immersive experience, simulating an astronaut's view of the sky from a distant planet, enhancing the storytelling aspect. 

NVDA integration for people with some kind of visual impairment. 

The project will feature educational content through informative pop-ups and audio descriptions, providing users with insights about celestial objects and exoplanetary systems, such as its shown in the example with Kepler. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## References

* [Gaia Data Release 3](https://www.cosmos.esa.int/web/gaia/data-release-3)
* [NVDA Documentation](https://scikit-learn.org/)
* [NVDA Executable for implementation on Godot](https://numpy.org/)
* [NVDA Implementation](https://pandas.pydata.org/)
* [NASA Heliophysics Information](https://matplotlib.org/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contact

Alejandro Sanz Ramirez - [Linkedin](https://www.linkedin.com/in/alejandro-sanz-ramirez-3b631a201/) - asanz2003@gmail.com

Tristán Ortiz Roset - [Linkedin](https://www.linkedin.com/in/tristan-ortiz-roset-ba2762221/) - tortiz.roset@gmail.com

Claudia Ortiz Roset - [Linkedin](https://www.linkedin.com/in/claudia-ortiz-roset) - claudia.or102@gmail.com 

Claudia Garcia Talavera - [Linkedin](https://www.linkedin.com/in/claudia-garc%C3%ADa-talavera-060289215) - claudiagatalavera@gmail.com

Jorge Jiménez Cabrera - [Linkedin](https://www.linkedin.com/in/jorge-jimenez-cabrera/) - jorge.kp10@gmail.com

Project Link: [https://github.com/asanzra/Sky-Wanderer-NASA-Space-Apps](https://github.com/asanzra/Sky-Wanderer-NASA-Space-Apps)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Video Demo

<!-- https://github.com/user-attachments/assets/49a90214-1aa5-4647-beba-91c0dab4ede1 -->

## Screenshots

![Alt Text](https://github.com/asanzra/Sky-Wanderer-NASA-Space-Apps/blob/main/Captura_info.png)




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/asanzra/Sky-Wanderer-NASA-Space-Apps.svg?style=for-the-badge
[contributors-url]: https://github.com/asanzra/Sky-Wanderer-NASA-Space-Apps/graphs/contributors
[stars-shield]: https://img.shields.io/github/stars/asanzra/Sky-Wanderer-NASA-Space-Apps.svg?style=for-the-badge
[stars-url]: https://github.com/asanzra/asanzra/Sky-Wanderer-NASA-Space-Apps/stargazers
[issues-shield]: https://img.shields.io/github/issues/asanzra/Sky-Wanderer-NASA-Space-Apps.svg?style=for-the-badge
[issues-url]: https://github.com/asanzra/Sky-Wanderer-NASA-Space-Apps/issues
[license-shield]: https://img.shields.io/github/license/asanzra/Sky-Wanderer-NASA-Space-Apps.svg?style=for-the-badge
[license-url]: https://github.com/asanzra/Sky-Wanderer-NASA-Space-Apps/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url1]: https://www.linkedin.com/in/alejandro-sanz-ramirez-3b631a201/
[linkedin-url2]: https://www.linkedin.com/in/tristan-ortiz-roset-ba2762221/
[linkedin-url3]: https://www.linkedin.com/in/claudia-ortiz-roset
[linkedin-url4]: https://www.linkedin.com/in/claudia-garc%C3%ADa-talavera-060289215
[linkedin-url5]: https://www.linkedin.com/in/jorge-jimenez-cabrera/
