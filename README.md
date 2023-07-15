# date-reformatter
使用 date-reformatter 可以自动将 txt 文档中 `YYYY/MM/DD` 格式的日期转换为 `MM/DD/YYYY` 格式。

## 功能演示
假设 `input.txt` 文件中的内容如下：
```
1;2023/1/2;9;Strong;With the help of her AI dog, a sixteen year-old girl must get her sick mother to another planet where a better life awaits.
2;2023/1/4;14;LAL;Born with a word from nothing, the creature must eat one of its own to survive.
3;2023/1/6;23;Gemini;A man suffering from amnesia searches for whispers of his past in a post-apocalyptic world, while being hunted by human-like "Agents".
```
运行脚本后，`output.txt` 文件中的内容将变为：
```
1;1/2/2023;9;Strong;With the help of her AI dog, a sixteen year-old girl must get her sick mother to another planet where a better life awaits.
2;1/4/2023;14;LAL;Born with a word from nothing, the creature must eat one of its own to survive.
3;1/6/2023;23;Gemini;A man suffering from amnesia searches for whispers of his past in a post-apocalyptic world, while being hunted by human-like "Agents".
```
日期从 `YYYY/MM/DD` 格式转换为了 `MM/DD/YYYY` 格式。

## 运行条件
请确保您的系统上安装了 Python 3.6 或更高版本。

## 使用方法
1. 将仓库克隆或下载到计算机上的一个目录中。
2. 修改 `start.command (Mac)` 或 `start.bat (Win)` 中的路径，以指向您存放 `date-reformatter.py` 脚本的目录。
3. 将要处理的文本保存为 `input.txt` 文件，并放在与脚本相同的目录中。
4. 双击运行 `start.command` 或 `start.bat` 脚本以执行 `date-reformatter.py` 脚本。
5. 结果将写入到同一目录下名为 `output.txt` 的文件中。
<br>

# date-reformatter
With date-reformatter, you can automatically convert dates in the `YYYY/MM/DD` format to the `MM/DD/YYYY` format in a txt document.

## Demo
Assuming the contents of the `input.txt` file are as follows:
```
1;2023/1/2;9;Strong;With the help of her AI dog, a sixteen year-old girl must get her sick mother to another planet where a better life awaits.
2;2023/1/4;14;LAL;Born with a word from nothing, the creature must eat one of its own to survive.
3;2023/1/6;23;Gemini;A man suffering from amnesia searches for whispers of his past in a post-apocalyptic world, while being hunted by human-like "Agents".
```
After running the script, the content of the `output.txt` file will be:
```
1;1/2/2023;9;Strong;With the help of her AI dog, a sixteen year-old girl must get her sick mother to another planet where a better life awaits.
2;1/4/2023;14;LAL;Born with a word from nothing, the creature must eat one of its own to survive.
3;1/6/2023;23;Gemini;A man suffering from amnesia searches for whispers of his past in a post-apocalyptic world, while being hunted by human-like "Agents".
```
The dates have been converted from the `YYYY/MM/DD` format to the `MM/DD/YYYY` format.

## Requirements
Make sure you have Python 3.6 or higher installed on your system.

## Usage
1. Clone or download the repository to a directory on your computer.
2. Modify the path in `start.command (Mac)` or `start.bat (Win)` to point to the directory where you store the `date-reformatter.py` script.
3. Save the text to be processed as an `input.txt` file and place it in the same directory as the script.
4. Double-click `start.command` or `start.bat` to execute the `date-reformatter.py` script.
5. The result will be written to a file named `output.txt` in the same directory.
