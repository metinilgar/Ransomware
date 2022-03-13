<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/MetinIlgar/Ransomware">
    <img src="/Images/logo.png" alt="Logo">
  </a>

  <h3 align="center">Ransomware</h3>

  <p align="center">
    A simple ransomware that can be used for educational and informational purposes and to understand its logic.
    <br />
    <a href="https://github.com/MetinIlgar/Ransomware"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/MetinIlgar/Ransomware">View Demo</a>
    ·
    <a href="https://github.com/MetinIlgar/Ransomware/issues">Report Bug</a>
    ·
    <a href="https://github.com/MetinIlgar/Ransomware/issues">Request Feature</a>
  </p>
</p>


<!-- TABLE OF CONTENTS -->
<details open="open">
	<summary><h2 style="display: inline-block">Table of Contents</h2></summary>
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
				<li><a href="#required-libraries">Required Libraries</a></li>
				<li><a href="#installation">Installation</a></li>
			</ul>
		</li>
		<li>
			<a href="#usage">Usage</a>
			<ul>
				<li><a href="#software-usage">Software usage</a></li>
			</ul>
		</li>
		<li><a href="#roadmap">Roadmap</a></li>
		<li><a href="#contributing">Contributing</a></li>
		<li><a href="#license">License</a></li>
		<li><a href="#authors">Authors</a></li>
	</ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

It is ransomware for educational and informational purposes. It can be used to encrypt files in any folder on the computer or in all personal folders.

<hr>

**`Be sure to read these before using the software:`**
* **The software has been made for informational and educational purposes. And it continues to be developed.**
* **It should not be used for any wrong or malicious use. The person who wrote the program has no responsibility for such uses.**
* **The program is under development. It is recommended that your experiments be done on a virtual machine.**
* **Do not run the program without examining the codes. Pay attention to the comment lines.**

<hr>

You can suggest changes by forking this repository and creating a pull request or opening an issue.

### Built With

* [cryptography](https://cryptography.io/en/latest/)
* [socket](https://docs.python.org/3/library/socket.html)
* [os](https://docs.python.org/3/library/os.html)


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Required Libraries

Type this command in the console to install the required libraries:
* [pip](https://pypi.org/project/pip/)
  ```sh
  $ pip install -r requirements.txt
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/MetinIlgar/Ransomware.git
   ```
2. Run the software
   * First run the server.
   ```sh
   python server.py 
   ```
   * Then run main.py.
   ```sh
   python main.py
   ```


<!-- USAGE EXAMPLES -->
## Usage
Attention! Do not use this software unconsciously.

### Software usage
1. The server must be run first.
2. Then main.py should be run.
3. After main.py is running, servers will be connected automatically.
4. You can see what can be done by typing the "help" command on the command line where the server is running.

* If you type "enc", all files under the destination folder will be encrypted.
* If you type "dec", all files under the destination folder will be decrypted.
* If you type "close" main.py will stop working.
* If you type "exit" both server and main.py will stop working.
* If you type "help", the commands you can use will appear.


<!-- ROADMAP -->
## Roadmap

* See the [open issues](https://github.com/MetinIlgar/Ransomware/issues) for a list of proposed features (and known issues).

* Take a look at the [commits](https://github.com/MetinIlgar/Ransomware/commits/main) to see the build stages of the program.


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- LICENSE -->
## License

Distributed under the MIT License. See [LICENSE](https://github.com/MetinIlgar/Ransomware/blob/main/LICENSE) for more information.


<!-- CONTACT -->
## Authors

* Metin Ilgar Mutlu

[![GitHub Logo](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/MetinIlgar)
![Instagram Logo](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white) 
![Twitter Logo](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white) 
