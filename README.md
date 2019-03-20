# 智能 Fintech 解决方案平台

各个组在这个文件夹下新建一个文件夹，来进行代码的存放、学习、开发、测试。

> 不要把此目录（即文件夹）作为提交的途径，而要作为你电脑中所有与此项目相关的文件（包括 jupyter notebook 等，不包括二进制可执行文件）的存放处，你可以编辑 .gitignore 来制定规则，使某些文件不被 git 跟踪。
> 每个文件夹是一个项目（或子项目），这个项目所需要的 PyPI 包应写在 requirements.txt 中，每行一个。

## 文件（夹）命名

.
├── README.md
├── crawler
│   ├── README.md
│   └── ...
├── nlp
│   ├── README.md
│   └── ...
└── ...

文件夹采用全小写字母，python 源代码文件采用全小写下划线连接格式，如 universal_spider.py，每个文件夹可配说明文档，应为纯文本（包括 markdown），命名为 README.md。

> 纯文本指的是一切可用文本编辑器打开的文件，例如所有代码文件、json 文件、txt 文件、markdown 文件、config 文件、csv 文件、html 文件、xml 文件。其中部分文件用特定的应用程序打开，可以进行处理及渲染，如 markdown、csv、html，而用 vscode 等代码编辑器打开时则作为纯文本来处理。

## 文件编码

一律采用 UTF-8，记事本容易产生编码问题，应改用 vscode 等。

> 在管理员 cmd 中输入以下代码快速安装 vscode：
    @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin" && choco feature enable -n allowGlobalConfirmation
    choco install vscode